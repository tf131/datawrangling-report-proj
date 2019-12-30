# adds (when possible) a document from here api to the refering database entry - if the here reply was empty, the item remains unchanged
import configparser

import requests
from pymongo import MongoClient
import logging

# load the configfile
config = configparser.ConfigParser()
config.read('../conf.ini')
api_key = config['api_keys']['here']

logging.basicConfig(level=logging.WARN)
URL = "https://geocoder.ls.hereapi.com/6.2/geocode.json?apikey=" + api_key + "&searchtext="


def get_mongodb_db(db_name):
    client = MongoClient(config['mongodb']['connection_string'])
    return client[db_name]


db = get_mongodb_db("restaurants")
collection = db["restaurants_basic"]
results = collection.find({})

for result in results:
    id = result["_id"]
    name = result["name"]
    address = result["address"]
    city = result["city"]

    searchtext = name + " " + address + " " + city
    r = requests.get(url=URL + searchtext)
    raw_data = r.json()
    try:
        data = raw_data['Response']['View'][0]['Result'][0]
        if 'Relevance' in data:
            collection.update_one({"_id": id}, {"$set": {"here_api_result": data}})
    except:
        logging.warning("No refs found for the searchtext: " + searchtext)