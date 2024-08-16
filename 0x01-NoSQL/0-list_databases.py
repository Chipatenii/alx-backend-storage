#!/usr/bin/env python3
"""
Module to list all databases in MongoDB.
"""

from pymongo import MongoClient

def list_databases():
    """
    Lists all databases in MongoDB and prints them.
    """
    client = MongoClient()
    databases = client.list_database_names()
    for db in databases:
        print(db)

if __name__ == "__main__":
    list_databases()
