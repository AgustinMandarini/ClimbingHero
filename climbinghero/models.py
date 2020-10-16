import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, VARCHAR
from climbinghero import db

# Create a custom JsonEncodedDict class in a file accessed by your models
#Enables JSON storage by encoding and decoding on the fly
class JSONEncodedDict(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if not value:
            return None
        return json.loads(value)

class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(60))

    country = db.relationship('Country', lazy=True)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(60), nullable=True)

    continent_id = db.Column(db.Integer, db.ForeignKey('continent.id'), nullable=False)

    province = db.relationship('Province', lazy=True)
    user = db.relationship('User', lazy=True)

class Province(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=True)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    sector = db.relationship('Sector', lazy=True)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    descr = db.Column(db.Text)
    getin = db.Column(db.Text)
    coord = db.Column(JSONEncodedDict)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    province_id = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=False)
    user_id_created = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_modified = db.Column(db.Integer, db.ForeignKey('user.id'))

    subsector = db.relationship('Subsector', lazy=True)
    route = db.relationship('Route', lazy=True)


class Subsector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    descr = db.Column(db.Text)
    getin = db.Column(db.Text)
    area = db.Column(JSONEncodedDict)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    user_id_created = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_modified = db.Column(db.Integer, db.ForeignKey('user.id'))

    route = db.relationship('Route', lazy=True)

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    leng = db.Column(db.Integer)
    pitch = db.Column(db.Integer)
    grade = db.Column(db.String(4), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    descr = db.Column(db.Text)
    equip = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    subsector_id = db.Column(db.Integer, db.ForeignKey('subsector.id'))
    user_id_created = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_modified = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    sector = db.relationship('Sector', lazy=True)
    subsector = db.relationship('Subsector', lazy=True)
    route = db.relationship('Route', lazy=True)
