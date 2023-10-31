import os


def get_env_or_default(name, default=None):
    if name in os.environ:
        return os.environ[name]
    return default


database_user = get_env_or_default("DB_USER")
database_host = get_env_or_default("DB_HOST")
database_port = get_env_or_default("DB_PORT")
database_password = get_env_or_default("DB_PASSWORD")
database_name = "whosale_platform"

IS_TESTING = get_env_or_default("IS_TESTING", False)
APP_PORT = get_env_or_default("APP_PORT")
APP_IS_DEBUG = get_env_or_default("APP_IS_DEBUG")

uri = "postgresql://{user}:{password}@{host}:{port}/{database_name}"
DATABASE_URI = uri.format(
    user=database_user,
    password=database_password,
    host=database_host,
    port=database_port,
    database_name=database_name,
)
