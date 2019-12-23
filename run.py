import json
import pandas as pd

from pymongo import MongoClient


def get_mongodb_db(db_name):
    client = MongoClient(
        "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/test?retryWrites=true&w=majority")
    return client[db_name]


db = get_mongodb_db(db_name="restaurants")
collection = db["restaurants_untouched"]

print(collection.estimated_document_count())
