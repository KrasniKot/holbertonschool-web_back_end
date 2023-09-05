#!/usr/bin/envn python3
"""This module contains schools_by_topic()"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools sharing a common topic"""
    return mongo_collection.find({"topics": topic})
