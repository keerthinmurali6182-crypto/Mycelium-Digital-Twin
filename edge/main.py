# edge/main.py
import paho.mqtt.client as mqtt
import json
import time
import random

# Configuration
BROKER = "localhost"
TOPIC = "eco/packaging/data"

# Initialize Client
client = mqtt.Client()

def connect_to_broker():
    try:
        client.connect(BROKER, 1883, 60)
        print("Edge Device connected to Broker.")
    except Exception as e:
        print(f"Connection failed: {e}")

def get_sensor_data():
    """Simulates data from a mycelium-integrated IoT sensor."""
    return {
        "box_id": "MYC-001",
        "temp_c": round(random.uniform(18.0, 26.0), 2),
        "structural_integrity": round(random.uniform(90.0, 100.0), 2),
        "timestamp": time.time()
    }

# Main Loop
connect_to_broker()
client.loop_start()

try:
    while True:
        data = get_sensor_data()
        client.publish(TOPIC, json.dumps(data))
        print(f"Sent: {data}")
        time.sleep(5) # Data sent every 5 seconds
except KeyboardInterrupt:
    client.loop_stop()
    print("Stopped.")