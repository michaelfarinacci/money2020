from app import db

#we need more info here. merchant name, location, category, cuisine, bill ammount, potentially items on bill,
#transaction time, 

class Merchant(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

class Transactions(db.model):
    id = db.Column(db.Integer, primary_key=True)
    card_num = db.Column(db.Integer())
    date = db.Column(db.DATETIME())
    total = db.Column(db.Integer())
    merchant = db.Column(db.DATETIME())
    merchant_id = db.Column(db.Integer, ForeignKey('merchants.id'))
    merchant = db.relationship(Merchant)
