from dupl_calc import google_places_api_quality_v2
import csv


# res = google_places_api_quality_v2.get_duplicates_list_of_lists()
# res2 = google_places_api_quality_v2.get_non_dpl()

def calc_precision(listGolddpl, listdpl):
    listGolddpl = get_gold_standard_dpl_list()
    TP = 0
    for elem in listdpl:
        if elem in listGolddpl:
            TP += 1
    return TP / len(listdpl)


def calc_recall(listGolddpl, listdpl):
    listGolddpl = get_gold_standard_dpl_list()
    TP = 0
    FN = 0
    for elem in listdpl:
        if elem in listGolddpl:
            TP += 1
    for elem in listGolddpl:
        if elem not in listdpl:
            FN += 1
    return TP / (TP + FN)


def get_gold_standard_dpl_list():
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


print(calc_precision(get_gold_standard_dpl_list(), google_places_api_quality_v2.get_duplicates_list_of_lists()))
print(calc_recall(get_gold_standard_dpl_list(), google_places_api_quality_v2.get_duplicates_list_of_lists()))
