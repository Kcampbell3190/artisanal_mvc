from init import db, ma
from marshmallow import fields


class User(db.Model):
    """help"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False) 
    #is_customer
    #product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

class UserSchema(ma.Schema):
    """Help"""
    users = fields.List(fields.Nested('UserSchema', exclude=['user']))
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'products')