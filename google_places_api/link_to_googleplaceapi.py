#adds (when possible) a document from google places api to the refering database entry - if the google places reply was empty, the item remains unchanged
import configparser
import json

import requests
from pymongo import MongoClient
import logging

# load the configfile
config = configparser.ConfigParser()
config.read('../conf.ini')

logging.basicConfig(level=logging.INFO)
google_places_api_key = config['api_keys']['googleplaces']
URL1 = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
URL2 = "&inputtype=textquery&fields=formatted_address,geometry,icon,name,permanently_closed,photos,place_id," \
       "plus_code,types,price_level,rating,user_ratings_total&key="


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
    r = requests.get(url=URL1 + searchtext + URL2 + google_places_api_key)
    raw_data = r.json()
    try:
        # take the first candidate from api reply
        data = raw_data['candidates'][0]
        logging.info(json.dumps(data))
        collection.update_one({"_id": id}, {"$set": {"google_place_search_api_result": data}})
    except:
        logging.warning("No refs found for the searchtext: " + searchtext)
