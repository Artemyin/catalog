from . import db

class Street(db.Model):
    __tablename__ = 'street'


class Building(db.Model):
    __tablename__ = 'building'


class Entrance(db.Model):
    __tablename__ = 'entrance'

class Floor(db.Model):
    __tablename__ = 'floor'


class Lamp(db.Model):
    __tablename__ = "lamp"