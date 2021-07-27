from . import db

class Street(db.Model):
    __tablename__ = 'street'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
     

class Building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100), unique=True, nullable=False)


class Entrance(db.Model):
    __tablename__ = 'entrance'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)


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
