__author__ = 'Beka'
from flango import db
from users.models import User, Product

db.create_all()

admin = User('admin','admin@gmail.com')
product = Product("snikersi")

db.session.add(admin)
db.session.add(product)

db.session.commit()


