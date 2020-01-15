import itertools


def get_duplicates_list_of_lists(mongodb_collection, matching_field):
    matching_field_with_starting_dollar_symbol = '$' + matching_field
    results = mongodb_collection.aggregate([
        {
            '$addFields': {
                'id_to_int': {
                    '$toInt': '$id'
                }
            }
        },
        {

            '$match': {
                matching_field: {
                    '$exists': 1
                }
            }
        }, {
            '$group': {
                '_id': matching_field_with_starting_dollar_symbol,
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

    return_list = list()

    for doc in results:
        doc = doc['id_array']
        if len(doc) > 2:
            # get all combinations
            comb = itertools.combinations(doc, 2)
            for itterator_comb in list(comb):
                itterator_comb = list(itterator_comb)
                itterator_comb.sort()
                return_list.append(itterator_comb)
        else:
            doc.sort()
            return_list.append(doc)
    return_list.sort()
    return return_list
