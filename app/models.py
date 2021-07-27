from . import db

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street_id = db.relationship('Street', backref='address', lazy=True)
    building_id = db.relationship('Building', backref='address', lazy=True)
    entrance_id = db.relationship('Entrance', backref='address', lazy=True)

class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
        nullable=False)
    #buildings = db.relationship('Building', backref='street', lazy=True)
     

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
        nullable=False)
    #street_name = db.Column(db.Integer, db.ForeignKey('street.id'),
    #    nullable=False)
    #entrances = = db.relationship('Entrance', backref='building', lazy=True)

class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
        nullable=False) 
    #building_number = db.Column(db.Integer, db.ForeignKey('building.id'),
    #    nullable=False)

''''
class Floor(db.Model):
    __tablename__ = 'floor'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
'''


class Lamp(db.Model):
    __tablename__ = "lamp"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    power = db.Column(db.Integer)
    #color
    #type
    #meanlife
