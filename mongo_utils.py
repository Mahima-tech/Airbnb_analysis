from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb+srv://mahimapcse:qe4QXo3ARFl3rrtR@airbnb0.askpykn.mongodb.net/?authMechanism=DEFAULT")
    return client.get_database('sample_mflix')

def get_collection(db, collection_name):
    return db[collection_name]
