from . import db
from flask_login._compat import unicode


class PropertyB(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(500))
    bedroomnum = db.Column(db.String(50))
    bathroomnum = db.Column(db.String(50))
    location=db.Column(db.String(500))
    price= db.Column(db.String(200))
    type= db.Column(db.String(150))
    description= db.Column(db.String(1000))
    filename=db.Column(db.String(200))

    def __init__(self, title, bedroomnum, bathroomnum, location, price, type, description, filename):
        self.title = title
        self.bedroomnum = bedroomnum
        self.bathroomnum = bathroomnum
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.filename=filename
    