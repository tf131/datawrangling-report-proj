# adds (when possible) a document from codio api to the refering database entry - if the codio reply was empty, the item remains unchanged
import configparser
import json

import requests
from pymongo import MongoClient
import logging

# load the configfile
config = configparser.ConfigParser()
config.read('../conf.ini')

logging.basicConfig(level=logging.INFO)
api_key = config['api_keys']['geocodio']
URL1 = "https://api.geocod.io/v1.4/geocode?q="


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
    # phone = result["phone"]

    searchtext = name + " " + address + " " + city
    logging.info(searchtext)
    u = (URL1 + searchtext + "&api_key=" + api_key)
    r = requests.get(url=URL1 + searchtext + "&api_key=" + api_key)
    raw_data = r.json()
    try:
        # take the first candidate from api reply
        data = str(raw_data['results'][0]['location'])
        logging.info(json.dumps(data))
        collection.update_one({"_id": id}, {"$set": {"geocodio_search_api_result": {'geolocation_as_string': data}}})
    except:
        logging.warning("No refs found for the searchtext: " + searchtext)
