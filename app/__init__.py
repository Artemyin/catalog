from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_admin import Admin


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

#admin = Admin(app, template_mode='bootstrap3')

from app.models import  Lamp, Street, Building, Entrance, AddressView, Address
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app, template_mode='bootstrap3')

  

admin.add_view(AddressView(Address, db.session))
admin.add_view(ModelView(Street, db.session))
admin.add_view(ModelView(Building, db.session))
admin.add_view(ModelView(Entrance, db.session))
admin.add_view(ModelView(Lamp, db.session))


