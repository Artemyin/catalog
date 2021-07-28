import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#FLASK_APP = 'app'
#FLASK_ENV= 'development'

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

FLASK_ADMIN_SWATCH = 'cerulean'