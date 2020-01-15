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

# implement logging
logging.basicConfig(level=logging.INFO)

# unique indexing for deduplication (dictionary)
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
    # get mongoDB collection object. Used for any further mongodb querys.
    mongodb_collection = get_mongodb_db_collection()
    # fill the mongodb collection with initial data from
    # https://hpi.de/naumann/projects/repeatability/datasets/restaurants-dataset.html
    initial_fill_database(mongodb_collection)
    # link database to api providers
    link_to_hereapi(mongodb_collection, api_key=config['api_keys']['here'])
    link_to_googleplaceapi(mongodb_collection, api_key=config['api_keys']['googleplaces'])
    link_to_geocodio(mongodb_collection, config['api_keys']['geocodio'])
    # calculate precision, recall and f1score
    calcer(mongodb_collection, unique_identifiers)

    # optional: plot location information to map (based on Google place search)
    # this should open a new browser window
    mapplot(mongodb_collection, api_key=config['api_keys']['mapbox'])


if __name__ == '__main__':
    import logging.config

    logging.basicConfig(level=logging.INFO)
    main()
