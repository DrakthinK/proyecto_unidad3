from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='root', password='root')

db = client['personaje']