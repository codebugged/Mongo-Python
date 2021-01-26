import pymongo
myclient = pymongo.MongoClient("mongodb+srv://sarthak:lucknow123@cluster0.jvetf.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)
for y in mycol.find():
	print(y)