from quality_validation import mongodb_pipeline_calls
import csv

matching_field_google_places_api = 'google_place_search_api_result.place_id'
matching_field_here_api = 'here_api_result.Location.LocationId'
matching_field_geocodio = 'geocodio_search_api_result.geolocation_as_string'


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


def get_gold_standard_dpl_list_from_data():
    elem_list = list()
    return_list_of_lists = list()
    with open('../data/restaurants_DPL.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            elem_list.append(int(row['id1']))
            elem_list.append(int(row['id2']))
            elem_list.sort()
            return_list_of_lists.append(elem_list.copy())
            elem_list.clear()
    return return_list_of_lists


# print(calc_precision(get_gold_standard_dpl_list_from_data(),
#                      mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_google_places_api)))
# print(calc_recall(get_gold_standard_dpl_list_from_data(),
#                   mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_google_places_api)))

print(calc_precision(get_gold_standard_dpl_list_from_data(),
                     mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_geocodio)))
print(calc_recall(get_gold_standard_dpl_list_from_data(),
                  mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_geocodio)))

# print(calc_precision(get_gold_standard_dpl_list_from_data(),
#                      mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_here_api)))
# print(calc_recall(get_gold_standard_dpl_list_from_data(),
#                   mongodb_pipeline_calls.get_duplicates_list_of_lists(matching_field_here_api)))
