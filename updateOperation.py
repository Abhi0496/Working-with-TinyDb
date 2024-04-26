from tinydb import TinyDB, Query
from app import db, Fruit



db.update({'count': 10}, Fruit.type == 'apple')
print(db.all())
