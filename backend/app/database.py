# backend/app/database.py
from pymongo import MongoClient

class DatabaseHandler:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['mycelium_db']
        self.collection = self.db['telemetry']