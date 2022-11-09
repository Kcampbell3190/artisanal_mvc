from init import db, ma
from marshmallow import fields


class Category(db.Model):
    """"Category"""
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    abiltiy = db.Column(db.String)

class ProductSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'description', 'ability',)