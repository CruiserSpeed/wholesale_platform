from database import *
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import bcrypt
import sys
from globals import (
    EMAIL_LOGIN,
    EMAIL_PASSWORD,
    EMAIL_CONFIRMATION_EMAIL_TEMPLATE,
    ADMIN_CONFIRMATION_EMAIL_TEMPLATE,
    CONFIRMATION_NOTIFICATION_EMAIL_TEMPLATE,
    SELF_URL,
)


class MailingManager():
    @staticmethod
    def compute_hash(text):
        encoded_text = text.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_text = bcrypt.hashpw(encoded_text, salt)
        return hashed_text.decode('utf-8')


    @staticmethod
    def check_hash(text, hashed_text):
        print(hashed_text, file=sys.stderr)
        return bcrypt.checkpw(text.encode('utf-8'), hashed_text.encode('utf-8'))


    @staticmethod
    def gen_hash(length=10):
        candidates = string.ascii_letters + string.digits
        return ''.join(random.choice(candidates) for _ in range(length))


    @staticmethod
    def create_admin_confirmation(email, approve_hash, refuse_hash):
        approve_link = SELF_URL.format(handle=f"registration/admin_confirm/{approve_hash}")
        refuse_link = SELF_URL.format(handle=f"registration/admin_confirm/{refuse_hash}")

        msg = MIMEText(ADMIN_CONFIRMATION_EMAIL_TEMPLATE.format(
            email=email,
            approve_link=approve_link,
            refuse_link=refuse_link
        ), "html", "utf-8")

        msg["Subject"] = Header("Новый админ", "utf-8")
        msg["From"] = EMAIL_LOGIN
        msg["To"] = ', '.join([EMAIL_LOGIN])
        return msg


    @staticmethod
    def create_email_confirmation(requesting_email, confirmation_hash):
        confirmation_link = SELF_URL.format(handle=f"registration/email_confirm/{confirmation_hash}")

        msg = MIMEText(EMAIL_CONFIRMATION_EMAIL_TEMPLATE.format(
            requesting_email=requesting_email,
            confirmation_link=confirmation_link,
        ), "html", "utf-8")

        msg["Subject"] = Header("Tradematch", "utf-8")
        msg["From"] = EMAIL_LOGIN
        msg["To"] = ', '.join([EMAIL_LOGIN])
        return msg

    @staticmethod
    def create_confirmation_notification(email, is_confirmed):
        if is_confirmed:
            resolution = "Ваша заявка подтверждена!"
        else:
            resolution = "Ваша заявка была отклонена"

        msg = MIMEText(CONFIRMATION_NOTIFICATION_EMAIL_TEMPLATE.format(
            resolution = resolution
        ), "html", "utf-8")

        msg["Subject"] = Header("Tradematch", "utf-8")
        msg["From"] = EMAIL_LOGIN
        msg["To"] = ', '.join([email])
        return msg

    @staticmethod
    def send_email(recepients, email):
        s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=100)
        try:
            s.starttls()
            s.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            s.sendmail(email["From"], recepients, email.as_string())
            print(f"Sended to {recepients}", file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)
            return False
        finally:
            s.quit()
        return True


mailing_manager = MailingManager()



