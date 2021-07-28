'''
from app.models import Address, Lamp
#from app import admin
from app import app
from app import db 

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app, template_mode='bootstrap3')

admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Lamp, db.session))
'''
