from flask import Blueprint
from init import db, bcrypt
#from datetime import date
from models.product import Product #ProductSchema
from models.user import User
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
    
    categories = [
        category (
             name = "Candles"
             description = "handmade candles by one of our artisans"
             abiltiy = "ASD, ADHD"
        )
         category (
             name = "Resume writing"
             description = "A professional writing service offered by one of our freelancers"
             abiltiy = "Dsylexia, Hearing difficulties"
        )
         category (
             name = "Artwork"
             description = "arts produced by one of our creatives"
             abiltiy = "wishes to not include"
        )
    ]
     db.session.add_all(categories)
    db.session.commit()

    orders = [
        order (
            user_id = "007"
            product_id = "123"
            amount = $50
            quantity = 1
            status = True

        )
        order (
            user_id = "008"
            product_id = "333"
            amount = 150
            quantity = 2
            status = True

        )
        order (
            user_id = "009"
            product_id = "222"
            amount = 30
            quantity = 3
            status = True

        )
    ]
    
    
     db.session.add_all(orders)
    db.session.commit()
    
    
    
    
    
    print("Tables seeded")
    
