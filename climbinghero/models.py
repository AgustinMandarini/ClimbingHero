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

class Sectors(db.Model):
    sector_id = db.Column(db.Integer, primary_key=True)
    area = db.Column(JSONEncodedDict)
