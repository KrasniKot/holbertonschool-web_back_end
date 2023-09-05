#!/usr/bin/env python3
"""This module contains insert_school()"""


def insert_school(mongo_collection, **kwargs):
    """Adds a new document into the given collection"""
    return mongo_collection.insert_one(kwargs)
