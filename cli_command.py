from flask import Blueprint
from init import db, ma, bcrypt
from models.product import Product #ProductSchema
from models.user import User
from models.order import Order
from models.categories import Category



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
            is_admin=True,
            is_customer= False
        ),
        User(
            name='John Cleese',
            email='someone@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8'),
            is_admin=True,
            is_customer= False
        ), 
         User(
            name='Kamram',
            email='k@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8'),
            is_admin=False,
            is_customer= True
        ), 

    ]

    db.session.add_all(users)
    db.session.commit()
    
    categories = [
        Category (
            
             name = "Candles",
             description = "handmade candles by one of our artisans",
             abiltiy = "ASD, ADHD"
        ),
         Category (
             name = "Resume writing",
             description = "A professional writing service offered by one of our freelancers",
             abiltiy = "Dsylexia, Hearing difficulties",
        ),
         Category (
             name = "Artwork",
             description = "arts produced by one of our creatives",
             abiltiy = "wishes to not include"
        ),
    ]
    db.session.add_all(categories)
    db.session.commit()

    products = [
       Product(
            user_id = "1",
            category_id = "1",
            title = "start first item",
            description = "stage 1 starting the products table",
            status = True,
            creative = "Lachlan and ASD"
           ),
    
        Product(
            user_id = "2",
            category_id = "2",
            title = "second item",
            description = "stage 2 seeding database",
            status = True,
            creative = "Jenny and ADHD",
           ),
        Product(
            user_id = "3",
            category_id = "3",
            title = "third item",
            description = "stage 3 seeding database",
            status = True,
            creative = "Jonathan and Depression"

        ),
    ]
    db.session.add_all(products)
    db.session.commit()
    

    orders = [
        Order (
            user_id = "1",
            product_id = "1",
            amount = 50,
            quantity = 1,
            status = True

        ),
        Order (
            user_id = "1",
            product_id = "1",
            amount = 150,
            quantity = 2,
            status = True

        ),
        Order (
            user_id = "1",
            product_id = "1",
            amount = 30,
            quantity = 3,
            status = True

        ),
    ]
    
    
    db.session.add_all(orders)
    db.session.commit()
    

    print("Tables seeded")
    
