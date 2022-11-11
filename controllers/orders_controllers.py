from flask import Blueprint, request
from init import db
from datetime import date
from models.order import Order, OrderSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/')
def all_orders():
  
     stmt = db.select(Order)
     orders = db.session.scalars(stmt).all()
     return OrderSchema(many=True).dump(orders)

@orders_bp.route('/<int:id>/')
def one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        return OrderSchema().dump(order)
    else: 
        return {'error': f'Order not found with id {id}'}, 404


@orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
  
    data = OrderSchema().load(request.json)

    order = Order(
        user_id = request.json['user_id'],
        product_id= request.json['product_id'],
        amount = request.json['amount'],
        status = request.json['status'],
        quantity = request.json['quantity'],
    )
    # Add and commit the user to the database
    db.session.add(order)
    db.session.commit()
    return OrderSchema().dump(order), 201
    

@orders_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_order(id):
   # authorize()

    stmt = db.select(Order).filter_by(id=id)
    order= db.session.scalar(stmt)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {'message': f"Order '{order.id}' deleted successfully"}
    else:
        return {'error': f'Order not found with id {id}'}, 404


@orders_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        order.user_id = request.json.get('user_id') or order.user_id
        order.product_id = request.json.get('product_id') or order.product_id
        order.status = request.json.get('status') or order.status
        order.amount = request.json.get('amount') or order.amount
        order.quantity = request.json.get('quantity') or order.quantity
        db.session.commit()      
        return OrderSchema().dump(order)
    else:
        return {'error': f'Order not found with id {id}'}, 404