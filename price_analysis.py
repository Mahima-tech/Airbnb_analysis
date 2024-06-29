from pymongo import MongoClient

# MongoDB connection parameters
MONGODB_URL = 'mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT'
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'listings'  # Adjust as per your collection name

def analyze_price_data():
    try:
        client = MongoClient(MONGODB_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # Example query: Get average price per room type
        pipeline = [
            {"$group": {"_id": "$room_type", "avg_price": {"$avg": "$price"}}}
        ]

        result = collection.aggregate(pipeline)

        for doc in result:
            print(doc)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        client.close()

if __name__ == "__main__":
    analyze_price_data()
