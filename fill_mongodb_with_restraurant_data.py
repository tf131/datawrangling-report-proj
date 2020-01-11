import csv
import logging


def initial_fill_database(mongodb_collection):
    logger = logging.getLogger(__name__)
    itemlist = []
    with open('data/restaurants.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            itemlist.append(row)

    result = (mongodb_collection.insert_many(itemlist))
    if result.acknowledged == True:
        logger.info("data insertion completed")
