from init import db, ma
from marshmallow import fields

class Order(db.Model):
    """"orders"""
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()
    product_id = db.Column()
    amount = db.Column(db.Integer, not null)
    quantity = db.Column(db.Integer, not null)
    status = db.Column(db.Boolean, default=False)

class OrderSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'user_id', 'product_id', 'description', 'status', 'amount', 'quantity',)