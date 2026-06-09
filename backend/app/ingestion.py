# backend/app/ingestion.py
import json
from .database import DatabaseHandler

class DataIngestor:
    def __init__(self):
        self.db = DatabaseHandler()

    def handle_message(self, client, userdata, msg):
        """This function processes the MQTT message."""
        payload = json.loads(msg.payload.decode())
        print(f"Received data: {payload}")
        
        # Save to MongoDB
        self.db.collection.insert_one(payload)
        print("Data successfully saved to MongoDB!")