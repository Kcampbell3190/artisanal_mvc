from init import db, ma
from marshmallow import fields


class User(db.Model):
    """User relation"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False) 
    is_customer = db.Column(db.Boolean, default=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)


class UserSchema(ma.Schema):
    """Help"""
    users = fields.List(fields.Nested('UserSchema', exclude=['user']))
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'products',)