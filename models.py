from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@52.36.203.109:5432/angel_db'
db = SQLAlchemy(app)

class Merchant(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.Integer)
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
    order_id = db.Column(db.Integer())
    card_num = db.Column(db.Integer())
    date = db.Column(db.DATETIME())
    total = db.Column(db.Integer())
    cashback_amount = db.Column(db.Integer())
    customer_since = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    tax_amount = db.Column(db.Integer())
    transaction_created_on = db.Column(db.Integer())
    tip_amount = db.Column(db.Integer())
    amount = db.Column(db.Integer())
    merchant_id = db.Column(db.Integer, ForeignKey('merchants.id'))
    merchant = db.relationship(Merchant)

    def __init__(self):
        pass