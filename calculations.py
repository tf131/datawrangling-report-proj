import mongodb_pipeline_calls
import csv

dict_apis = [{'google_places_api': 'google_place_search_api_result.place_id'},
             {'here_api': 'here_api_result.Location.LocationId'},
             {'geocodio_api': 'geocodio_search_api_result.geolocation_as_string'}]


# calculate the precision for a goldstandard list of duplicate and a predicted list of duplicates
def calc_precision(listGolddpl, listdpl):
    listGolddpl = get_gold_standard_dpl_list_from_data()
    TP = 0
    for elem in listdpl:
        if elem in listGolddpl:
            TP += 1
    return TP / len(listdpl)


def calc_recall(listGolddpl, listdpl):
    listGolddpl = get_gold_standard_dpl_list_from_data()
    TP = 0
    FN = 0
    for elem in listdpl:
        if elem in listGolddpl:
            TP += 1
    for elem in listGolddpl:
        if elem not in listdpl:
            FN += 1
    return TP / (TP + FN)


def calc_f1_score(listGolddpl, listdpl):
    return (2 * (calc_recall(listGolddpl, listdpl) * calc_precision(listGolddpl, listdpl)) / (
            calc_recall(listGolddpl, listdpl) + calc_precision(listGolddpl, listdpl)))


def get_gold_standard_dpl_list_from_data():
    elem_list = list()
    return_list_of_lists = list()
    with open('data/restaurants_DPL.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            elem_list.append(int(row['id1']))
            elem_list.append(int(row['id2']))
            elem_list.sort()
            return_list_of_lists.append(elem_list.copy())
            elem_list.clear()
    return return_list_of_lists


def calcer(mongodb_collection, dict_apis):
    for elem in dict_apis:
        for key, value in elem.items():
            print(key + ' Precision result ' + str(calc_precision(get_gold_standard_dpl_list_from_data(),
                                                                  mongodb_pipeline_calls.get_duplicates_list_of_lists(
                                                                      mongodb_collection,
                                                                      value))))
            print(key + ' Recall result ' + str(calc_recall(get_gold_standard_dpl_list_from_data(),
                                                            mongodb_pipeline_calls.get_duplicates_list_of_lists(
                                                                mongodb_collection,
                                                                value))))
            print(key + ' f1 score result ' + str(calc_f1_score(get_gold_standard_dpl_list_from_data(),
                                                                mongodb_pipeline_calls.get_duplicates_list_of_lists(
                                                                    mongodb_collection,
                                                                    value))))
