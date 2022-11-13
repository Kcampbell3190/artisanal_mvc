from marshmallow import fields

from init import db, ma


class Category(db.Model):
    """"Category"""
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    ability = db.Column(db.String)

    
class CategorySchema(ma.Schema):
    category = fields.List(fields.Nested('CategorySchema', exclude=['category']))
    class Meta: 
        fields = ('id', 'name', 'description', 'ability',)