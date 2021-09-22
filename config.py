import os

class Config:
    NAME = "Base"

    _basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    DEVELOPMENT = False

    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

    DATABASE_CONNECT_OPTIONS = {}

    FLASK_ADMIN_SWATCH = 'cerulean'

    # Flask-Security config
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"


    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"

    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"

    # Flask-Security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    NAME = "Production"
    pass


class StagingConfig(Config):
    NAME = "Staging"
    DEBUG = True


class DevelopmentConfig(Config):
    NAME = "Development"
    DEBUG = True
    DEVELOPMENT = True