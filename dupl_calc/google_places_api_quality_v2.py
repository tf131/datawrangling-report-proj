import configparser
import csv
import logging
import itertools

import pandas as pd
from pymongo import MongoClient

# configure logging
logging.basicConfig(level=logging.DEBUG)

# load the configfile
config = configparser.ConfigParser()

config.read('../conf.ini')


def get_mongodb_db(db_name):
    client = MongoClient(config['mongodb']['connection_string'])
    return client[db_name]


def get_duplicates_list_of_lists():
    db = get_mongodb_db("restaurants")
    collection = db["restaurants_basic"]
    results = collection.aggregate([
        {
            '$addFields': {
                'id_to_int': {
                    '$toInt': '$id'
                }
            }
        },
        {

            '$match': {
                'google_place_search_api_result.place_id': {
                    '$exists': 1
                }
            }
        }, {
            '$group': {
                '_id': '$google_place_search_api_result.place_id',
                'counter': {
                    '$sum': 1
                },
                'id_array': {
                    '$addToSet': '$id_to_int'
                }
            }
        }, {
            '$sort': {
                'counter': -1
            }
        }, {
            '$match': {
                'counter': {
                    '$gt': 1
                }
            }
        }, {
            '$project': {
                'id_array': 1,
                '_id': 0
            }
        }

    ])

    empty_list = list()

    for doc in results:
        doc = doc['id_array']
        if len(doc) > 2:
            # get all combinations
            comb = itertools.combinations(doc, 2)
            for itterator_comb in list(comb):
                itterator_comb = list(itterator_comb)
                itterator_comb.sort()
                empty_list.append(itterator_comb)
        else:
            doc.sort()
            empty_list.append(doc)
    empty_list.sort()
    return empty_list


def get_non_dpl_list_of_lists():
    db = get_mongodb_db("restaurants")
    collection = db["restaurants_basic"]
    pipeline = [
        {

            '$match': {
                'google_place_search_api_result.place_id': {
                    '$exists': 1
                }
            }
        },
        {
            '$addFields': {
                'id_to_int': {
                    '$toInt': '$id'
                }
            }
        }, {
            '$project': {
                'id_to_int': 1,
                'google_place_search_api_result.place_id': 1,
                '_id': 0
            }
        }
    ]
    results = collection.aggregate(pipeline)
    list_of_elements_raw = list()
    for elem in results:
        list_of_elements_raw.append(elem)
    list_of_nonnuplicate_elements = list()
    return_list_of_non_duplicate_pairs = list()
    for i in list_of_elements_raw:
        for j in list_of_elements_raw:
            if i['google_place_search_api_result']['place_id'] != j['google_place_search_api_result']['place_id']:
                id_i = i['id_to_int']
                id_j = j['id_to_int']
                list_of_nonnuplicate_elements.append(id_i)
                list_of_nonnuplicate_elements.append(id_j)
                list_of_nonnuplicate_elements.sort()
                if list_of_nonnuplicate_elements not in return_list_of_non_duplicate_pairs:
                    return_list_of_non_duplicate_pairs.append(list_of_nonnuplicate_elements.copy())
                list_of_nonnuplicate_elements.clear()
        print("yo")
    return_list_of_non_duplicate_pairs.sort()
    return return_list_of_non_duplicate_pairs


def get_non_dpl_with_where_operator():
    # pymongo.errors.OperationFailure: $where is not allowed in this atlas tier
    db = get_mongodb_db("restaurants")
    collection = db["restaurants_basic"]
    result = collection.find(
        {"$where": "this.google_place_search_api_result.place_id==this.google_place_search_api_result.place_id"})
    return result
