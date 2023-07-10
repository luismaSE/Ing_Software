import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://microblog:microblog1234@cluster0.7houovt.mongodb.net/?retryWrites=true&w=majority')
print(client.server_info())
dbs = client.list_database_names()
print("sin", dbs)

# db = client[os.getenv('DATABASE_NAME')]

# dbs = client.list_database_names()

# print(dbs)