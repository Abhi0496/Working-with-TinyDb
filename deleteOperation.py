from tinydb import TinyDB,Query
from app import db, Fruit

db.remove(Fruit.count < 5)
print(db.all())

db.truncate()
print(db.all())