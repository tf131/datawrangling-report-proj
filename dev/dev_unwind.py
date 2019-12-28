import pprint

from pymongo import MongoClient


def get_mongodb_db(db_name):
    client = MongoClient(
        "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/test?retryWrites=true&w=majority")
    return client[db_name]


db = get_mongodb_db("testdb")
collection = db["unwind_collection"]
d = dict()
d.update({"matrnr": 12345, "name": "Lisa Simpson", "classes": ["DMDB", "KBAN", "DMMR"]})
#collection.insert_one(d)
results = collection.aggregate([{"$unwind": "$classes"}])

for elem in results:
    pprint.pprint(elem)


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