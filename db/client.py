from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/stock')

models = dict({'reports': client.reports})
