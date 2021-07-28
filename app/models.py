from app import db

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street_id = db.relationship('Street', backref='address', lazy='dynamic')
    building_id = db.relationship('Building', backref='address', lazy='dynamic')
    entrance_id = db.relationship('Entrance', backref='address', lazy='dynamic')
    lamp_id = db.relationship('Lamp', backref='address', lazy='dynamic')

    
class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
 
    def __repr__(self):
        return '<Street %r>' % (self.name) 

    def __init__(self, name=None):
        self.name = name
        

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    
    def __repr__(self):
        return '<Building %r>' % (self.number)

    def __init__(self, number=None):
        self.number = number


class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id')) 

    def __repr__(self):
        return '<Entrance %r>' % (self.number) 

    def __init__(self, number=None):
        self.number = number

class Lamp(db.Model):
    __tablename__ = "lamp"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id')) 

    def __repr__(self):
        return '<Lamp %r>' % (self.name) 

    def __init__(self, name=None):
        self.name = name