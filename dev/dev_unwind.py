import pprint

from pymongo import MongoClient


def get_mongodb_db(db_name):
    client = MongoClient(
        "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/test?retryWrites=true&w=majority")
    return client[db_name]


db = get_mongodb_db("testdb")
collection = db["unwind_collection"]
d = dict()
d.update({"matrnr": 12345, "name": "Lisa Simpson", "classes": ["DMDB", "KBAN", "DMMR"]})
#collection.insert_one(d)
results = collection.aggregate([{"$unwind": "$classes"}])

for elem in results:
    pprint.pprint(elem)
