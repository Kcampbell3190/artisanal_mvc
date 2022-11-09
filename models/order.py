from init import db, ma
from marshmallow import fields

class Order(db.Model):
    """"orders"""
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    