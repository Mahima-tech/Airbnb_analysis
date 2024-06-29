from pymongo import MongoClient
import datetime

# MongoDB connection parameters
MONGODB_URL = 'mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT'
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'comments'  # Adjust as per your collection name

def check_availability(date_range):
    try:
        client = MongoClient(MONGODB_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        query = {
            "date_field": {"$gte": date_range[0], "$lte": date_range[1]}
        }

        result = collection.find(query)
        availability_count = result.count()

        print(f"Availability count: {availability_count}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        client.close()

if __name__ == "__main__":
    # Example: Check availability for a specific date range
    date_range = [datetime.datetime(2024, 7, 1), datetime.datetime(2024, 7, 7)]
    check_availability(date_range)
