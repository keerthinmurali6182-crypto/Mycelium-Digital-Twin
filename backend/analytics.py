
from pymongo import MongoClient



def generate_report():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['mycelium_db']
    collection = db['telemetry']

    # Retrieve all records
    total_records = collection.count_documents({})
    
    # Simple Logic: Assume 2kg CO2 saved per package
    CO2_SAVED_PER_BOX = 2.0
    total_co2_saved = total_records * CO2_SAVED_PER_BOX

    print("--- SUSTAINABILITY IMPACT REPORT ---")
    print(f"Total Packages Tracked: {total_records}")
    print(f"Total CO2 Offset: {total_co2_saved} kg")
    print(f"System Status: {'OPTIMAL' if total_records > 0 else 'WAITING FOR DATA'}")
    print("------------------------------------")

if __name__ == "__main__":
    generate_report()