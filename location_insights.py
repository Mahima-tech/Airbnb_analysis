from pymongo import MongoClient

# MongoDB connection parameters
MONGODB_URL = 'mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT'
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'locations'  # Adjust as per your collection name

def get_location_insights():
    try:
        client = MongoClient(MONGODB_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # Example query: Get average ratings by location
        pipeline = [
            {"$group": {"_id": "$location", "avg_rating": {"$avg": "$rating"}}}
        ]

        result = collection.aggregate(pipeline)

        for doc in result:
            print(doc)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        client.close()

if __name__ == "__main__":
    get_location_insights()
