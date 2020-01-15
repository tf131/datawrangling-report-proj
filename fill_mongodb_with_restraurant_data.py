import csv
import logging


def initial_fill_database(mongodb_collection):
    logger = logging.getLogger(__name__)
    item_list = []
    with open('data/restaurants.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            item_list.append(row)

    result = (mongodb_collection.insert_many(item_list))
    if result.acknowledged == True:
        logger.info("data insertion completed")
