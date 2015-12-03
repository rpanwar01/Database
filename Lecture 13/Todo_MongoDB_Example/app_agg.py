import pymongo
from pymongo import MongoClient
from bson.son import SON

db = MongoClient().todo
results = list(db.items.aggregate( [
   {"$group": {"_id": "$status", "count": {"$sum": 1}}},
] ))
for result in results:
    if result["_id"] == 0:
        print("Completed task :", result["count"])
    if result["_id"] == 1:
        print("Not completed task :", result["count"])
