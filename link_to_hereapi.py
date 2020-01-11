# adds (when possible) a document from here api to the refering database entry - if the here reply was empty, the item remains unchanged
import configparser

import requests
import logging


def link_to_hereapi(mongodb_collection, api_key):
    logger = logging.getLogger(__name__)
    url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?apikey=" + api_key + "&searchtext="

    results = mongodb_collection.find({})

    for result in results:
        id = result["_id"]
        name = result["name"]
        address = result["address"]
        city = result["city"]

        searchtext = name + " " + address + " " + city
        logger.info("searchtext is: " + searchtext)
        r = requests.get(url=url + searchtext)
        if r.status_code != 200:
            logger.error("HTTP status code: " + r.status_code)

        raw_data = r.json()
        try:
            data = raw_data['Response']['View'][0]['Result'][0]
            if 'Relevance' in data:
                mongodb_collection.update_one({"_id": id}, {"$set": {"here_api_result": data}})
        except:
            logger.warning("No refs found for the searchtext or API not configured properly: " + searchtext)
