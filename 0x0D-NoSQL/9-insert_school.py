#!/usr/bin/env python3
""" pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """ insert  document in mongo collection
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
