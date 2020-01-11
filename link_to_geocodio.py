# adds (when possible) a document from codio api to the refering database entry - if the codio reply was empty, the item remains unchanged
import configparser
import json

import requests
from pymongo import MongoClient
import logging


def link_to_geocodio(mongodb_collection, api_key):
    global raw_data
    logger = logging.getLogger(__name__)
    URL1 = "https://api.geocod.io/v1.4/geocode?q="

    results = mongodb_collection.find({})

    for result in results:
        id = result["_id"]
        name = result["name"]
        address = result["address"]
        city = result["city"]
        # phone = result["phone"]

        searchtext = name + " " + address + " " + city
        logger.info("searchtext is: " + searchtext)
        u = (URL1 + searchtext + "&api_key=" + api_key)
        try:
            r = requests.get(url=URL1 + searchtext + "&api_key=" + api_key)
            if r.status_code != 200:
                logger.error("HTTP status code: " + str(r.status_code))
            raw_data = r.json()
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            logger.error(e)

        try:
            # take the first candidate from api reply
            data = str(raw_data['results'][0]['location'])

            mongodb_collection.update_one({"_id": id},
                                          {"$set": {"geocodio_search_api_result": {'geolocation_as_string': data}}})
        except:
            logger.warning("No refs found for the searchtext or API not configured properly: " + searchtext)
