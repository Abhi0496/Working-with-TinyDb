from app import db 

#TinyDB expects the data to be Python dicts

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})