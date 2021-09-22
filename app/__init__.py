import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig") #Config Production
app.config.from_object(env_config)

db = SQLAlchemy(app)

from app import views


