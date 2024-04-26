from tinydb import TinyDB, Query

db = TinyDB('db.json')
# We now have a TinyDB database that stores its data in db.json


Fruit = Query()
#Creating a Query object for querying