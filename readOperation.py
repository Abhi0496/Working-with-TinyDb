from tinydb import Query
from app import db, Fruit

#Either we can read entire data
#print(db.all())
"""
[{'type': 'apple', 'count': 7}, {'type': 'peach', 'count': 3}]
"""

# Or iterate over it
#for item in db:
#    print(item)
"""
{'type': 'apple', 'count': 7}
{'type': 'peach', 'count': 3}
"""

#We can also search for specifics
print(db.search(Fruit.type == 'peach'))
print(db.search(Fruit.count > 5))

