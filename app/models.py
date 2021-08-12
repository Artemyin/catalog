from flask_admin.contrib.sqla import ModelView

from app import db

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    entrance_id = db.Column(db.Integer, db.ForeignKey('entrance.id')) 
    lamp_id =  db.Column(db.Integer, db.ForeignKey('lamp.id'))


    def __init__(self, street_name, building_num, entrance_num):
        street = Street.query.filter_by(street_name=street_name).first()
        if not street:
            street = Street(street_name=street_name)
            db.session.add(street)
        self.street_id = street.id

        building = Building.query.filter_by(building_number=building_num).first()
        if not building:
            building = Building(building_number=building_num)
            db.session.add(building)
        self.building_id = building.id

        entrance = Entrance.query.filter_by(entrance_number=entrance_num).first()
        if not entrance:
            entrance = Entrance(entrance_number=entrance_num)
            db.session.add(entrance)
        self.entrance_id = entrance.id
        db.session.commit()
        # addr = Address(street=street, building=building, entrance=entrance)


class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.relationship('Address', backref='street', lazy='dynamic')
     
    def __repr__(self):
        return '<Street %r>' % (self.street_name) 

    def __init__(self, street_name):
        self.street_name = street_name
        

class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    building_number = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.relationship('Address', backref='building', lazy='dynamic')
    
    def __repr__(self):
        return '<Building %r>' % (self.building_number)

    def __init__(self, building_number):
        self.building_number = building_number


class Entrance(db.Model):
    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    entrance_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.relationship('Address', backref='entrance', lazy='dynamic')

    def __repr__(self):
        return '<Entrance %r>' % (self.entrance_number) 

    def __init__(self, entrance_number):
        self.entrance_number = entrance_number


class Lamp(db.Model):
    __tablename__ = "lamp"

    id = db.Column(db.Integer, primary_key=True)
    lamp_name = db.Column(db.String(100), unique=True, nullable=False)
    address_id = db.relationship('Address', backref='lamp', lazy='dynamic')
    
    def __repr__(self):
        return '<Lamp %r>' % (self.lamp_name) 

    def __init__(self, lamp_name):
        self.lamp_name = lamp_name


roles_users_table = db.Table('roles_users',
                            db.Column('users_id', db.Integer(), db.ForeignKey('users.id')),
                            db.Column('roles_id', db.Integer(), db.ForeignKey('roles.id')))

# Define models for the users and user roles
class Roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())

    roles = db.relationship('Roles', secondary=roles_users_table, backref='user', lazy=True)
