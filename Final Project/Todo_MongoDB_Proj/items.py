import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.todo
db1 = client.todo_arc

def signup_data(name, email, pswd):
    db.items.insert({'name': name, 'email': email, 'pswd': pswd, 'task': "", 'status': 2})    

def check_login(username, password):
    items = db.items.find_one({'name':username})
    if items: 
        if items['pswd'] == password:
            return True
        return False
    else:
        return False
        
def get_items(user, status = -1):
    if (status >= 0):
        items = db.items.find({'status':status, 'name':user})
    else:
        items = db.items.find({'status':{ "$lt": 2}, 'name':user})
    items = [ item for item in items ]
    for item in items:
        item["id"] = str(item["_id"])
        item["_id"] = None
    return items
    
def new_item(task, status, user):
    db.items.insert({'name': user, 'task': task, 'status': status})
    
def get_item(id):
    item = db.items.find_one({"_id":ObjectId(id)})
    if (item):
        item["id"] = str(item["_id"])
        item["_id"] = None
    return item

def get_arc_item(id):
    item = db1.items.find_one({"_id":ObjectId(id)})
    if (item):
        item["id"] = str(item["_id"])
        item["_id"] = None
    return item
    
def save_item(item):
    id = ObjectId(item['id'])
    db.items.update_one(
        {"_id":id},
        {"$set":{
            "task":item["task"],
            "status":item["status"]
        }}
    )

def discard_item(id):
    id = ObjectId(id)
    item = db.items.find_one({"_id": id}) 
    db1.items.insert(item)  
    db.items.delete_one({"_id":id})

def discard_items(user):
    items = db.items.find({'status':{ "$lt": 2}, 'name':user}) 
    for item in items:
        db1.items.insert(item)
    db.items.remove({'status':{ "$lt": 2}, 'name':user})
  
def get_arc_items(user):
    items = db1.items.find({'name':user})
    items = [ item for item in items ]
    for item in items:
        item["id"] = str(item["_id"])
        item["_id"] = None
    return items

def save_arc_items(item, user):
    db.items.insert({'name': user, 'task': item["task"], 'status': 1})
    
def del_arc_items(id, user):
    id = ObjectId(id)
    db1.items.delete_one({"_id":id,'name':user})
    
          
if __name__ == "__main__":
    db.items.delete_many({})
    print(get_items())
    new_item("more really new stuff",0)
    new_item("another really, really new stuff",1)
    items = get_items(-1)
    id = None
    for item in items:
        print (item)
        id = str(item["id"])        
    print("----")
    print(id)
    print ('-----')
    item = get_item(id)
    print(item)
    item['task'] = "new version:" + item['task']
    print(item)
    save_item(item)
    print(item)