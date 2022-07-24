

import pymongo

client = pymongo.MongoClient("mongodb+srv://shriya91:JAna851991@cluster0.7i14p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

db = client.test
d= {
    "name" : "shriya",
    "mail-id":"shriya@gmail.com",
    "subject" : ["DS", "big data", "data analytics"]
}

db1 = client['myinfo']
coll = db1['sudh']
coll.insert_one(d)

