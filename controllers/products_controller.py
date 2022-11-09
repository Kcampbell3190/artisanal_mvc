from flask import Blueprint, request
from init import db
from datetime import date
from models.product import Product, ProductSchema


products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')

def all_products():
  
     stmt = db.select(Product)
     products = db.session.scalars(stmt).all()
     return ProductSchema(many=True).dump(products)

@products_bp.route('/<int:id>/')
def one_product(id):
    stmt = db.select(Product).filter_by(id=id)
    products = db.session.scalar(stmt)
    if product:
        return ProductSchema(many=True).dump(products)
    else: 
        return {'error': f'Product not found with id {id}'}, 404


@products_bp('/', methods=['POST'])
@jwt_required()
def create_product():
  
    data = ProductSchema().load(request.json)

    product = Product(
        title = request.json['title'],
        description = request.json['description'],
        date = date.today(),
        status = request.json['status'],
        creative = request.json['creative'],
    )
    # Add and commit the user to the database
    db.session.add(product)
    db.session.commit()
    return ProductSchema().dump(product), 201
    

@products_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_card(id):
    authorize()

    stmt = db.select(Product).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        db.session.delete(card)
        db.session.commit()
        return {'message': f"Product '{product.title}' deleted successfully"}
    else:
        return {'error': f'Product not found with id {id}'}, 404
