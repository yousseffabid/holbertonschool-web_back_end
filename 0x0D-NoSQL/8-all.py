#!/usr/bin/env python3
""" list all pymongo
"""


def list_all(mongo_collection):
    """ list all documents in a collection
    """
    documents = mongo_collection.find()
    return documents
