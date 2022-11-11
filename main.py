from flask import Flask
from init import db, ma, bcrypt, jwt
from cli_command import db_commands
from controllers.auth_controllers import auth_bp
from controllers.categories_controller import categories_bp
from controllers.orders_controllers import orders_bp
from controllers.products_controller import products_bp

import os






def create_app():
    app = Flask(__name__)

    # @app.errorhandler(404)
    # def not_found():
    #     return {'error': str('err')}, 404

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config ['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

   

   # app.register_blueprint(products_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(products_bp)

    return app

