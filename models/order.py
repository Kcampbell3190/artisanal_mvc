from init import db, ma
from marshmallow import fields

class Order(db.Model):
    """"orders"""
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True) 
    amount = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False) 

class OrderSchema(ma.Schema):
    """"schema"""
    class Meta: 
        '''Meta'''
        fields = ('id', 'user_id', 'product_id', 'description', 'status', 'amount', 'quantity',)