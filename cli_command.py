from flask import Blueprint
from init import db, bcrypt
#from datetime import date
from models.product import Product, ProductSchema
from models.user import User, UserSchema
#from models.user import User
#from models.comment import Comment


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Cleese',
            email='someone@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()
    products = [
       Product(
            title = "start first item",
            description = "stage 1 starting the products table",
            status = True,
            creative = "Lachlan and ASD"
           ),
    
        Product(
            title = "second item",
            description = "stage 2 seeding database",
            status = True,
            creative = "Jenny and ADHD",
           ),
        Product(
            title = "third item",
            description = "stage 3 seeding database",
            status = True,
            creative = "Jonathan and Depression"

        ),
    ]
    db.session.add_all(products)
    db.session.commit()
    print("Tables seeded")
    
