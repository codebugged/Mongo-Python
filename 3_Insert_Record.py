import pymongo
myclient = pymongo.MongoClient("mongodb+srv://sarthak:lucknow123@cluster0.jvetf.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "Sarthak", "address": "Highway_37" }
x = mycol.insert_one(mydict)