from app import db

class Merchant(db.Model):
    __tablename__ 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

     def __init__(self, name):
         self.name = name

class User(db.model)
    __tablename__ 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
