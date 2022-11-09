from init import db, ma






class Product(db.Model):
    """product table"""
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    status = db.Column(db.Boolean)
    creative = db.Column(db.String)

class ProductSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'title', 'description', 'status', 'creative', 'date',)

