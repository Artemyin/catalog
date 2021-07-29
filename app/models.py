from flask_admin.contrib.sqla import ModelView

from app import db

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    entrance_id = db.Column(db.Integer, db.ForeignKey('entrance.id')) 
    lamp_id =  db.Column(db.Integer, db.ForeignKey('lamp.id')) 


class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.relationship('Address', backref='street', lazy='dynamic')
     
    def __repr__(self):
        return '<Street %r>' % (self.street_name) 

    def __init__(self, street_name=None):
        self.street_name = street_name
        

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    building_number = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.relationship('Address', backref='building', lazy='dynamic')
    
    def __repr__(self):
        return '<Building %r>' % (self.building_number)

    def __init__(self, building_number=None):
        self.building_number = building_number


class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    entrance_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.relationship('Address', backref='entrance', lazy='dynamic')

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

