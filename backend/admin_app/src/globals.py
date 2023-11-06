import os

def get_env_or_default(name, default=None):
    if name in os.environ:
        return os.environ[name]
    return default

admin_confirmation_email_file = open("src/assets/admin_confirmation_email.html", "r")
ADMIN_CONFIRMATION_EMAIL_TEMPLATE = admin_confirmation_email_file.read()
admin_confirmation_email_file.close()
email_confirmation_email_file = open("src/assets/email_confirmation_email.html", "r")
EMAIL_CONFIRMATION_EMAIL_TEMPLATE = email_confirmation_email_file.read()
email_confirmation_email_file.close()
confirmation_notification_email_file = open("src/assets/confirmation_notification_email.html", "r")
CONFIRMATION_NOTIFICATION_EMAIL_TEMPLATE = confirmation_notification_email_file.read()
confirmation_notification_email_file.close()

database_user = get_env_or_default("DB_USER")
database_host = get_env_or_default("DB_HOST")
database_port = get_env_or_default("DB_PORT")
database_password = get_env_or_default("DB_PASSWORD")
database_name = "whosale_platform"

EMAIL_LOGIN = get_env_or_default("EMAIL_LOGIN")
EMAIL_PASSWORD = get_env_or_default("EMAIL_PASSWORD")

API_WALKER_HOST = get_env_or_default("API_WALKER_HOST")
API_WALKER_PORT = get_env_or_default("API_WALKER_PORT")

IS_TESTING = get_env_or_default("IS_TESTING", False)
APP_PORT = get_env_or_default("APP_PORT")
APP_IS_DEBUG = get_env_or_default("APP_IS_DEBUG")

SELF_URL = "http://127.0.0.1:5000/{handle}"
SELF_URL_WITH_CGI = SELF_URL + "?{cgi}"

uri = "postgresql://{user}:{password}@{host}:{port}/{database_name}"
DATABASE_URI = uri.format(
    user=database_user,
    password=database_password,
    host=database_host,
    port=database_port,
    database_name=database_name,
)
