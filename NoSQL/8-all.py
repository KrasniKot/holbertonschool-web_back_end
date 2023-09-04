#!/usr/bin/env python3
"""This Module contains list_all()"""


def list_all(mongo_collection):
    """Lists all the documents in a collection"""
    return mongo_collection.find()
