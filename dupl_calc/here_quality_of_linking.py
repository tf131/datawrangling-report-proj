import configparser
import csv
import itertools
import pandas as pd

from pymongo import MongoClient

# https://developer.here.com/documentation/geocoder/dev_guide/topics/scoring.html

# load the configfile
config = configparser.ConfigParser()

config.read('../conf.ini')


def get_mongodb_db(db_name):
    client = MongoClient(config['mongodb']['connection_string'])
    return client[db_name]


def get_dpl_df():
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
                'here_api_result.Location.Address': {
                    '$exists': 1
                }
            }
        }, {
            '$group': {
                '_id': '$here_api_result.Location.LocationId',
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

    list_of_duplicates = list()
    df = pd.DataFrame(results)

    for index, row in df.iterrows():
        for elem in row:
            perm = itertools.combinations(elem, 2)
            for p in list(perm):
                tmplist_for_converting_from_tuple = list(p)
                tmplist_for_converting_from_tuple.sort()
                list_of_duplicates.append(tmplist_for_converting_from_tuple)
    list_of_duplicates.sort(key=lambda i: i[0])

    return pd.DataFrame(list_of_duplicates, columns=['id1', 'id2'])
