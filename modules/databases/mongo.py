import logging
from pymongo import MongoClient
from modules.app.config import settings

class MONGODB:
    """ Class for MONGODB Connection Management"""
    url: str

    def __init__(self, url):
        self.url = url

    def connect(self):
        """ Mongo Connection Function"""
        try:
            connection = MongoClient(self.url)
            print("Connected to MONGODB")
            return connection
        except Exception as err:
            print(f"Failed to connect to MONGODB: {err}")


mongo_cli = MONGODB(url=settings.MONGO_URL)
# Connect to Mongo
mongo_conn = mongo_cli.connect()
