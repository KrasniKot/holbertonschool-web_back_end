#!/usr/bin/env python3
"""This module provides some stats about Nginx logs in the mongo db"""

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient("mongodb://127.0.0.1:27017")
    coll = client.logs.nginx

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(coll.count_documents({}))
    print("Methods:")

    for m in method:
        print(f"\tmethod {m}: {coll.count_documents({'method': m})}")

    print(coll.count_documents({"method": "GET", "path": "/status"}))
