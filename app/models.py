from os import name
from app import db

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)

    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))
    street = db.relationship('Street', backref=db.backref('street', lazy='subquery'))

    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    building = db.relationship('Building', backref=db.backref('building', lazy='subquery'))
    
    entrance_id = db.Column(db.Integer, db.ForeignKey('entrance.id')) 
    entrance = db.relationship('Entrance', backref=db.backref('entrance', lazy='subquery'))

    lamp_id =  db.Column(db.Integer, db.ForeignKey('lamp.id'))
    lamp = db.relationship('Lamp', backref=db.backref('lamp', lazy='subquery'))


    def __init__(self, street_name, building_name, entrance_name):
        street = Street.query.filter_by(name=street_name).first()
        if not street:
            street = Street(name=street_name)
            db.session.add(street)
        self.street_id = street.id

        building = Building.query.filter_by(name=building_name).first()
        if not building:
            building = Building(name=building_name)
            db.session.add(building)
        self.building_id = building.id

        entrance = Entrance.query.filter_by(name=entrance_name).first()
        if not entrance:
            entrance = Entrance(name=entrance_name)
            db.session.add(entrance)
        self.entrance_id = entrance.id
        
        db.session.commit()
        


class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
     
    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name):
        self.name = name
        

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    
    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name):
        self.name = name


class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True, nullable=False)
    

    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name):
        self.name = name


class Lamp(db.Model):
    __tablename__ = "lamp"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    
    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name):
        self.name = name

