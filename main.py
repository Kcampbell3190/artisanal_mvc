from flask import Flask
from init import db, ma
from controllers.products_controller import products_bp
import os






def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found():
        return {'error': str(err)}, 404

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(products_bp)

    return app

