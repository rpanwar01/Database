import pymongo
from pymongo import MongoClient
from bson.son import SON
db = MongoClient().aggregation_example

#result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
#                                 {"x": 2, "tags": ["cat"]},
#                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
#                                 {"x": 3, "tags": []}])
#result.inserted_ids
pipeline = [
     {"$unwind": "$tags"},
     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
     {"$sort": SON([("count", -1), ("_id", -1)])}
 ]
print ("List:", list(db.things.aggregate(pipeline)))
print ("plan for this aggregation:", db.command('aggregate', 'things', pipeline=pipeline, explain=True))