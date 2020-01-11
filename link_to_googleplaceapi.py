# adds (when possible) a document from google places api to the refering database entry - if the google places reply was empty, the item remains unchanged
import configparser
import json

import requests
from pymongo import MongoClient
import logging


def link_to_googleplaceapi(mongodb_collection, api_key):
    logger = logging.getLogger(__name__)
    URL1 = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    URL2 = "&inputtype=textquery&fields=formatted_address,geometry,icon,name,permanently_closed,photos,place_id," \
           "plus_code,types,price_level,rating,user_ratings_total&key="

    results = mongodb_collection.find({})

    for result in results:
        _id = result["_id"]
        name = result["name"]
        address = result["address"]
        city = result["city"]
        # phone = result["phone"]

        searchtext = name + " " + address + " " + city
        r = requests.get(url=URL1 + searchtext + URL2 + api_key)
        if r.status_code != 200:
            logger.error("HTTP status code: " + r.status_code)
        raw_data = r.json()
        logger.info("searchtext is: " + searchtext)
        try:
            # take the first candidate from api reply
            data = raw_data['candidates'][0]
            mongodb_collection.update_one({"_id": _id}, {"$set": {"google_place_search_api_result": data}})
        except:
            logger.warning("No refs found for the searchtext or API not configured properly: " + searchtext)
