from init import db, ma
from marshmallow import fields





class Product(db.Model):
    """product table"""
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    status = db.Column(db.Boolean)
    creative = db.Column(db.String)


    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    #order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


class ProductSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'title', 'description', 'status', 'creative', 'date',)

