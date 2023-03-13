#!/usr/bin/env python3
""" pymongo
"""


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools
        having a specific topic
    """
    return mongo_collection.find({"topics": topic})
