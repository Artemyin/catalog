from app import db
from flask_admin.contrib.sqla import ModelView

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street_id = db.relationship('Street', backref='address', lazy='dynamic')
    building_id = db.relationship('Building', backref='address', lazy='dynamic')
    entrance_id = db.relationship('Entrance', backref='address', lazy='dynamic')
    lamp_id =  db.Column(db.Integer, db.ForeignKey('lamp.id')) 


class AddressView(ModelView):
    form_columns = ['id', 'street_id', 'building_id', 'entrance_id', 'lamp_id']  


class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
 
    def __repr__(self):
        return '<Street %r>' % (self.street_name) 

    def __init__(self, street_name=None):
        self.street_name = street_name
        

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    building_number = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    
    def __repr__(self):
        return '<Building %r>' % (self.number)

    def __init__(self, building_number=None):
        self.building_number = building_number


class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    entrance_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id')) 

    def __repr__(self):
        return '<Entrance %r>' % (self.entrance_number) 

    def __init__(self, entrance_number=None):
        self.entrance_number = entrance_number


class Lamp(db.Model):
    __tablename__ = "lamp"

    id = db.Column(db.Integer, primary_key=True)
    lamp_name = db.Column(db.String(100), unique=True, nullable=False)

    address_id = db.relationship('Address', backref='lamp', lazy='dynamic')
    

    def __repr__(self):
        return '<Lamp %r>' % (self.lamp_name) 

    def __init__(self, lamp_name=None):
        self.lamp_name = lamp_name

