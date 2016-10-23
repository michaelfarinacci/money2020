from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@52.36.203.109:5432/angel_db_3'
db = SQLAlchemy(app)

class Merchant(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.Integer())
    category = db.Column(db.String())

    def __init__(self, name):
        self.name = name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    merchant_id = db.Column(db.Integer, ForeignKey('merchants.id'))
    merchant = db.relationship(Merchant)

    def __init__(self):
        pass

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String())
    card_num = db.Column(db.Integer())
    date = db.Column(db.DateTime())
    total = db.Column(db.Integer())
    cashback_amount = db.Column(db.Integer())
    customer_since = db.Column(db.DateTime())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    tax_amount = db.Column(db.Integer())
    transaction_created_on = db.Column(db.String())
    tip_amount = db.Column(db.Integer())
    amount = db.Column(db.Integer())
    merchant_id = db.Column(db.Integer, ForeignKey('merchants.id'))
    merchant = db.relationship(Merchant)

class HighSpendersPredictions(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    merchant_id = db.Column(db.Integer, ForeignKey('merchants.id'))
    # Represents how likely a user is to spend more with this merchant
    # if they get a coupon or reward. Value is between 0.0 and 1.0. The higher the more likely
    # the user is to spend more with the reward.
    score = db.Column(db.Float)
