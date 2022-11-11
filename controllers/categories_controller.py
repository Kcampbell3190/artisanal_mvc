from flask import Blueprint, request
from init import db, bcrypt, jwt
from datetime import date
from models.categories import Category, CategorySchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

@categories_bp.route('/')

def all_categories():
  
     stmt = db.select(Category)
     categories = db.session.scalars(stmt).all()
     return CategorySchema(many=True).dump(categories)

@categories_bp.route('/<int:id>/')
def one_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        return CategorySchema().dump(category)
    else: 
        return {'error': f'Category not found with id {id}'}, 404


@categories_bp.route('/create/', methods=['POST'])
@jwt_required()
def create_category():
  
    data = CategorySchema().load(request.json)

    category = Category(
       category_id = request.json['category_id'],
        name = request.json['name'],
        description = request.json['description'],
        ability = request.json['ability'],
    )
    # Add and commit the user to the database
    db.session.add(category)
    db.session.commit()
    return CategorySchema().dump(category), 201
    

@categories_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_category(id):
    authorize()

    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        db.session.delete(category)
        db.session.commit()
        return {'message': f"Category '{category.name}' deleted successfully"}
    else:
        return {'error': f'Category not found with id {id}'}, 404


@categories_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        category.category_id = request.json.get('category_id') or product.category_id
        category.description = request.json.get('description') or category.description
        category.name= request.json.get('name') or category.name
        db.session.commit()      
        return CategorySchema().dump(categories)
    else:
        return {'error': f'Category not found with id {id}'}, 404