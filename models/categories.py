from marshmallow import fields

from init import db, ma


class Category(db.Model):
    """"Category"""
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    ability = db.Column(db.String)

    #product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

class CategorySchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'ability',)