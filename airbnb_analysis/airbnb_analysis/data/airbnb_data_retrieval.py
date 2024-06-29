import pandas as pd
from pymongo import MongoClient

# MongoDB connection parameters
MONGODB_URL = 'mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT'
DB_NAME = 'sample_mflix'
COLLECTIONS = ['comments', 'embedded_movies', 'movies', 'sessions', 'theaters', 'users']

def retrieve_data_from_mongodb(collection_name):
    # Connect to MongoDB Atlas
    client = MongoClient(MONGODB_URL)
    db = client[DB_NAME]
    collection = db[collection_name]

    # Retrieve data from collection
    data = list(collection.find())

    # Close MongoDB connection
    client.close()

    return data

def save_to_csv(data, collection_name):
    # Convert retrieved data to pandas DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to CSV file
    file_path = f'C:/Users/Lenovo/Desktop/airbnb_analysis/airbnb_analysis/data/{collection_name}_raw_data.csv'
    df.to_csv(file_path, index=False)
    print(f"{collection_name} raw data saved successfully at {file_path}.")

if __name__ == "__main__":
    for collection_name in COLLECTIONS:
        # Retrieve data from MongoDB
        data = retrieve_data_from_mongodb(collection_name)

        # Save data to CSV
        save_to_csv(data, collection_name)
