import mongodb_pipeline_calls
import csv


# calculate the precision for a goldstandard list of duplicate and a predicted list of duplicates

def calc_precision(goldstandard_duplicates_list, duplicates_list):
    goldstandard_duplicates_list = get_gold_standard_dpl_list_from_data()
    TP = 0
    for elem in duplicates_list:
        if elem in goldstandard_duplicates_list:
            TP += 1
    return TP / len(duplicates_list)

# calculate the recall for a goldstandard list of duplicate and a predicted list of duplicates

def calc_recall(goldstandard_duplicates_list, duplicates_list):
    goldstandard_duplicates_list = get_gold_standard_dpl_list_from_data()
    TP = 0
    FN = 0
    for elem in duplicates_list:
        if elem in goldstandard_duplicates_list:
            TP += 1
    for elem in goldstandard_duplicates_list:
        if elem not in duplicates_list:
            FN += 1
    return TP / (TP + FN)

# calculate the f1 score for a goldstandard list of duplicate and a predicted list of duplicates

def calc_f1_score(goldstandard_duplicates_list, duplicates_list):
    return (2 * (calc_recall(goldstandard_duplicates_list, duplicates_list) * calc_precision(
        goldstandard_duplicates_list, duplicates_list)) / (
                    calc_recall(goldstandard_duplicates_list, duplicates_list) + calc_precision(
                goldstandard_duplicates_list, duplicates_list)))

# loads the restaurants_DPL.tsv file and returns a list with the all pairs
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

#calculation function
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
