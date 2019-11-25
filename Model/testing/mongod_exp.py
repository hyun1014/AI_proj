from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["myNewDB"]
test_insert_collection = db.testcase
