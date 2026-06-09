# backend/main.py
import paho.mqtt.client as mqtt
from app.ingestion import DataIngestor

# 1. Initialize the Ingestor
ingestor = DataIngestor()

# 2. Initialize the MQTT Client (with Callback API version fix)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) 

# 3. Assign the callback
client.on_message = ingestor.handle_message

# 4. Connect and Subscribe
client.connect("localhost", 1883, 60)
client.subscribe("eco/packaging/data")

print("Backend Ingestor is now listening for data...")
client.loop_forever()