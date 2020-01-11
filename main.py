import configparser
import logging
from fill_mongodb_with_restraurant_data import initial_fill_database
from calculations import calcer
from link_to_hereapi import link_to_hereapi
from link_to_googleplaceapi import link_to_googleplaceapi
from link_to_geocodio import link_to_geocodio
from pymongo import MongoClient
from visualization.mapbox_plot import mapplot

# load the configfile
config = configparser.ConfigParser()
config.read('./conf.ini')

# logging
logging.basicConfig(level=logging.INFO)

# unique index dictionary
unique_identifiers = [{'google_places_api': 'google_place_search_api_result.place_id'},
                      {'here_api': 'here_api_result.Location.LocationId'},
                      {'geocodio_api': 'geocodio_search_api_result.geolocation_as_string'}]


def get_mongodb_db_collection():
    mongo_database_name = config['mongodb']['database_name']
    client = MongoClient(config['mongodb']['connection_string'])
    db = client[mongo_database_name]
    collection = db["restaurants_basic"]
    return collection


def main():
    # get a collection from mongoDB
    mongodb_collection = get_mongodb_db_collection()
    # fill_database
    # initial_fill_database(mongodb_collection)
    # linkDatabase
    # link_to_hereapi(mongodb_collection, api_key=config['api_keys']['here'])
    # link_to_googleplaceapi(mongodb_collection, api_key=config['api_keys']['googleplaces'])
    # link_to_geocodio(mongodb_collection, config['api_keys']['geocodio'])
    calcer(mongodb_collection, unique_identifiers)

    # optional
    mapplot(mongodb_collection, api_key=config['api_keys']['mapbox'])


if __name__ == '__main__':
    import logging.config

    logging.basicConfig(level=logging.INFO)
    main()
