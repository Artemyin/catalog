"""
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from app.models import  Lamp, Street, Building, Entrance, Address, AddressView

admin = Admin(app, template_mode='bootstrap3')
 

admin.add_view(AddressView(Address, db.session))
admin.add_view(ModelView(Street, db.session))
admin.add_view(ModelView(Building, db.session))
admin.add_view(ModelView(Entrance, db.session))
admin.add_view(ModelView(Lamp, db.session))
"""