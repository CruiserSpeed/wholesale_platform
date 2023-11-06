from main import app
from flask import (
    request,
    render_template
)
import json
from database.models import (
    db,
    Admin,
    Confirmation
)
from api_walker.api_walker import send_request_to_api_walker
from flask_expects_json import expects_json
from jsonschema import validate
from managers.common_manager import common_manager
from managers.mailing_manager import mailing_manager
import sys
from string_constants import *

@app.route("/api_walker", methods=["GET"])
def send_api_walker():
    return send_request_to_api_walker()


@app.route("/registration/sign_in", methods=["POST"])
@expects_json({
    "type" : "object",
    "properties" : {
        JF_EMAIL : {"type" : "string"},
        JF_PASSWORD : {"type" : "string"},
    },
    "required": [JF_EMAIL, JF_PASSWORD]
})
def sign_in():
    def create_result(json_value):
        if json_value not in [JV_ADMIN_NOT_CONFIRMED,
                       JV_EMAIL_NOT_CONFIRMED,
                       JV_ADMIN_REFUSED,
                       JV_INVALID_CREDENTIALS,
                       JV_SUCCESS,
                       JV_ERROR]:
            print(f"UNKNOWN JSON VALUE: {json_value}", file=sys.stderr)
            return {JF_RESULT: JV_ERROR}
        return {JF_RESULT: json_value}

    data = json.loads(request.data)

    email: str = data[JF_EMAIL]
    password: str = data[JF_PASSWORD]

    admin = Admin.query.filter_by(email=email).first()

    if admin is None:
        return create_result(JV_INVALID_CREDENTIALS)

    if admin.email_confirmation_status != ST_CONFIRMED:
        return create_result(JV_EMAIL_NOT_CONFIRMED)

    if admin.admin_confirmation_status is None:
        return create_result(JV_ADMIN_NOT_CONFIRMED)

    if admin.admin_confirmation_status in [None, ST_REFUSED]:
        return create_result(JV_ADMIN_REFUSED)
    
    if admin.admin_confirmation_statue != ST_APPROVED:
        return create_result(JV_ERROR)

    if not common_manager.check_hash(password, admin.password):
        return create_result(JV_INVALID_CREDENTIALS)

    return create_result(JV_SUCCESS)



@app.route("/registration/sign_up", methods=["POST"])
@expects_json({
    "type" : "object",
    "properties" : {
        JF_EMAIL : {"type" : "string"},
        JF_PASSWORD : {"type" : "string"},
    },
    "required": [JF_EMAIL, JF_PASSWORD]
})
def sign_up():
    def create_reply(json_value):
        if json_value not in [JV_SUCCESS,
                            JV_ALREADY_EXISTS,
                            JV_ERROR]:
            print(f"UNKNOWN JSON VALUE: {json_value}", file=sys.stderr)
            return {JF_RESULT: JV_ERROR}
        return {JF_RESULT: json_value}

    data = json.loads(request.data)
    admin = Admin()
    admin.email = data[JF_EMAIL]
    admin.password = common_manager.compute_hash(data[JF_PASSWORD])

    res = Admin.query.filter_by(email=admin.email).first()
    if res is not None:
        return create_reply(JV_ALREADY_EXISTS)

    confirmation_hash = common_manager.gen_hash()
    email_confirmation = Confirmation()
    email_confirmation.hash = confirmation_hash
    email_confirmation.admin = admin
    db.session.add(email_confirmation)
    db.session.commit()

    email = mailing_manager.create_email_confirmation(requesting_email=admin.email, confirmation_hash=confirmation_hash)
    if not mailing_manager.send_email([admin.email], email):
        return create_reply(JV_ERROR)

    return create_reply(JV_SUCCESS)


@app.route("/registration/email_confirm/<hash>", methods=["GET"])
def email_confirm(hash):
    def create_reply(json_value):
        if json_value not in [JV_SUCCESS,
                            JV_ERROR]:
            print(f"UNKNOWN JSON VALUE: {json_value}", file=sys.stderr)
            return {JF_RESULT: JV_ERROR}
        return {JF_RESULT: json_value}

    conf = Confirmation.query.filter_by(hash=hash).first()

    if conf is None:
        return render_template("confirmation_page.html", msg="Something went wrong")

    admin = conf.admin
    conf.admin.email_confirmation_status = ST_CONFIRMED
    db.session.commit()
    for conf in admin.confirmations:
        db.session.delete(conf)
        db.session.commit()

    approve_hash = common_manager.gen_hash()
    admin_approve = Confirmation()
    admin_approve.hash = approve_hash
    admin_approve.admin = admin
    admin_approve.value = ST_APPROVED
    db.session.add(admin_approve)
    db.session.commit()

    refuse_hash = common_manager.gen_hash()
    admin_refuse = Confirmation()
    admin_refuse.hash = refuse_hash
    admin_refuse.admin = admin
    admin_refuse.value = ST_REFUSED
    db.session.add(admin_refuse)
    db.session.commit()

    email = mailing_manager.create_admin_confirmation(admin.email, approve_hash=approve_hash, refuse_hash=refuse_hash)
    if not mailing_manager.send_email([EMAIL_], email):
        return create_reply(JV_ERROR)
    return render_template("confirmation_page.html", msg="Confirmed!")


@app.route("/registration/admin_confirm/<hash>", methods=["GET"])
def admin_confirm(hash):

    conf = Confirmation.query.filter_by(hash=hash).first()

    if conf is None:
        return render_template("confirmation_page.html", msg="Something went wrong")

    admin = conf.admin
    if conf.value == ST_APPROVED:
        is_confirmed = True
        admin.admin_confirmation_state = ST_APPROVED
    elif conf.value == ST_REFUSED:
        is_confirmed = False
        admin.admin_confirmation_state = ST_REFUSED
    else:
        return render_template("confirmation_page.html", msg="Something went wrong")

    for conf in admin.confirmations:
        db.session.delete(conf)
        db.session.commit()

    email = mailing_manager.create_confirmation_notification(admin.email, is_confirmed=is_confirmed)
    if not mailing_manager.send_email([admin.email], email):
        return render_template("confirmation_page.html", msg="Something went wrong")
    
    if is_confirmed:
        return render_template("confirmation_page.html", msg="Confirmed!")
    return render_template("confirmation_page.html", msg="Dismissed!")


@app.route("/database/get_all", methods=["GET"])
def database_get_all():
    users = Admin.query.all()
    res = json.dumps([{"name": user.email, "password": user.password, "confirmed": user.confirmation_status} for user in users])
    return res
