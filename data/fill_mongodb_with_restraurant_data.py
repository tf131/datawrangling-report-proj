# This script imports the data from the restaurant to mongodb


import configparser
import csv
import json

from pymongo import MongoClient

# load the configfile
config = configparser.ConfigParser()
config.read('../conf.ini')


def get_mongodb_db(db_name):
    client = MongoClient(config['mongodb']['connection_string'])
    return client[db_name]


db = get_mongodb_db("restaurants")
collection = db["restaurants_basic"]

itemlist = []
with open('restaurants.tsv') as tsvfile:
    reader = csv.DictReader(tsvfile, dialect='excel-tab')
    for row in reader:
        itemlist.append(row)

result = (collection.insert_many(itemlist))
if result.acknowledged == True:
    print("data insertion completed")
