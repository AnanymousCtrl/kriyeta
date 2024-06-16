from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or switch to the database
db = client['loginApp']

# Create the collection
users_collection = db['users']

# Verify creation by inserting a test document
users_collection.insert_one({"test": "test"})
