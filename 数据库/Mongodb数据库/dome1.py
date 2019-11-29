import pymongo
# from pymongo import MongoClient
# client = MongoClient('119.23.145.20',27017)
myclient = pymongo.MongoClient("mongodb://119.23.145.20:27017/")
db = myclient.admin
db.authenticate("root", "sp123456|admin",mechanism='SCRAM-SHA-1')
mydb = myclient["audit"]
mycol = mydb["td_wk_request_log"]

 
x = mycol.find_one()
 
print(x)


# myclient = pymongo.MongoClient('mongodb://root:123456@localhost:27017/')

# for x in mycol.find():
#   print(x)


# python连接MongoDB踩过的坑
# https://www.jianshu.com/p/7437666f93e5



