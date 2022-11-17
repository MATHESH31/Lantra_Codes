import time

import pymongo

start = time.time()

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000")
    myclient.server_info()
    print("Database is connected.")
except:
    print("Connection Error!!")
print("Database Ping : ",time.time() - start)

mydb = myclient["Entertainment"]

mycol = mydb["movies"]

myclient.close()