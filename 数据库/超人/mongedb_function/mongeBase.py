import pymongo
import json
import urllib.parse
myclient = pymongo.MongoClient("mongodb://119.23.145.20:27017/")
# 查看集合名，即库名
# a = myclient.database_names()
# print(a)

# 先跑通，让mongedb存有数据，再通过修改参数的方式设计用例场景

class Mongedbtest(object):
	"""修改mongedb所要用的方法"""
	def __init__(self):
		super(Mongedbtest, self).__init__()
	def test1(self):
		# 调试代码
		print('success！！！')
	def face_compare(self,x,url):
		# 人脸对比度修改方法，x代表分数,只能输入数字;url代表身份证正面照片地址
		# 打开mongedb对应的数据库
		mydb = myclient['service']
		mycol = mydb['apilog_aliyun']
		# 设置要修改的参数
		b = {"confidence":x,"thresholds":[61.0,69.0,75.0],"rectA":[125,37,550,638],"rectB":[656,150,161,206],"errno":0,"request_id":"5f1bbcea-9c5b-4a49-b231-c851642782c3"}
		# 将参数进行转换为json格式即str字符串才能存入mongedb
		c = json.dumps(b,ensure_ascii=False)
		# print(c)  # 调试打印
		# 设置查询内容相当于SQL中的where后的语句，根据身份证正面照片查询
		myfix = {"img_url2" : url}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"result" : c}}
		mycol.update_many(myfix,new_values)
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print("正面照片地址: %s\n修改后的分数值: %s" % (x['img_url2'],x['result']))


	def mobileOnline(self,code,desc,phone):
		# 在网时长
		mydb = myclient['service']
		mycol = mydb['apilog_juhe']
		# 设置要修改的参数
		b = {
		    "idnum" : "",
	        "name" : "",
	        "mobile" : "15500000078",
	        "res" : 1,
	        "code" : code,
	        "desc" : desc,
	        "province" : "吉林省",
	        "city" : "长春市",
	        "isp" : "联通"
		}
		print(b)
		print(type(b))
		# # 设置查询内容相当于SQL中的where后的语句
		myfix = {'phone':phone,"function" : "mobileOnline"}
		# # 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"result" : b}}
		mycol.update_one(myfix,new_values)	


	def wkCheck(self,finalDecision,idcard):
		# 白骑士审查
		# 打开mongedb对应的数据库
		mydb = myclient['test_third']
		mycol = mydb['log']
		# 设置要修改的参数，白骑士状态描述
		b = {
		    "finalDecision" : finalDecision,
		}
		# print(b) # 调试
		# print(type(b))
		# 设置查询内容相当于SQL中的where后的语句
		myfix = {'type':'wk','idcard': idcard}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"content" : b}}
		mycol.update_many(myfix,new_values)
		# 打印修改后的结果
		for x in mycol.find(myfix):
			print('姓名:%s 手机号:%s 身份证号:%s\n修改后的状态:%s' % (x['name'],x['mobile'],x['idcard'],x['content']))	

	def tdCheck(self,final_score,idcard):
		# 同盾审查
		# 打开mongedb对应的数据库
		mydb = myclient['test_third']
		mycol = mydb['log']
		# 设置要修改的参数
		b = {
		    "final_score" : final_score,
		}
		# print(b) # 调试
		# print(type(b))
		# 设置查询内容相当于SQL中的where后的语句
		myfix = {'type':'td','idcard': idcard}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"content" : b}}
		mycol.update_many(myfix,new_values)
		# 打印修改后的结果
		for x in mycol.find(myfix):
			print('姓名:%s 手机号:%s 身份证号:%s\n修改后的状态:%s' % (x['name'],x['mobile'],x['idcard'],x['content']))	

	def onlineStatus(self,mobile_online_status_info,phone):
		# 联系人号码在网状态
		# 打开mongedb对应的数据库
		mydb = myclient['service']
		mycol = mydb['apilog_tongdun_bodyguard']
		# 设置要修改的参数
		b = {
		    "success" : "true",
	        "id" : "WF2018092914394216923609",
	        "result_desc" : {
	            "AUTHENTICATION_INFOQUERY" : {
	                "MobileOnlineStatus" : {
	                    "mobile_online_status_consistence" : 0,
	                    "mobile_online_status_info" : mobile_online_status_info
	                }
	            }
	        }
		}
		# print(b) # 调试
		# print(type(b))
		# 设置查询内容相当于SQL中的where后的语句
		myfix = {'phone': phone,'type':'getPhoneOnlineStatus'}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"result" : b}}
		mycol.update_one(myfix,new_values)
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print(x)		

class integration_result(object):
	"""第三方整合结果:月消费档次，手机号在网时长，手机号在网状态，身份证实名认证"""
	def __init__(self):
		super(integration_result, self).__init__()
	def integration_onlineStatus(self,mobile,onlineStatus_type):
		# 修改【手机号在网状态】数据
		# 打开mongedb对应的数据库
		mydb = myclient['audit']
		mycol = mydb['mobile_party']

		# 查询手机号在网状态
		myfix = {'mobile': mobile,"function" : "onlineStatus"}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"type" : onlineStatus_type}}
		mycol.update_many(myfix,new_values)
		
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print('联系人手机号:%s 类型:%s from:%s 状态:%s\n' % (x['mobile'],x['function'],x['from'],x['type']))

	def integration_spendLevel(self,mobile,spendLevel_type):
		# 修改【月消费档次】数据
		# 打开mongedb对应的数据库
		mydb = myclient['audit']
		mycol = mydb['mobile_party']

		# 根据手机号查询
		myfix = {'mobile': mobile,"function" : "spendLevel"}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"type" : spendLevel_type}}
		mycol.update_one(myfix,new_values)
		
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print('联系人手机号:%s 类型:%s from:%s 状态:%s\n' % (x['mobile'],x['function'],x['from'],x['type']))

	def integration_checkCard(self,idcard,checkCard_type):
		# 修改【身份证实名认证】数据
		# 打开mongedb对应的数据库
		mydb = myclient['audit']
		mycol = mydb['mobile_party']

		# 根据手机号查询
		myfix = {'idcard': idcard,"function" : "checkCard"}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"type" : checkCard_type}}
		mycol.update_one(myfix,new_values)
		
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print(x)
	def integration_mobileOnline(self,mobile,mobileOnline_type):
		# 修改【手机号在网时长】数据
		# 打开mongedb对应的数据库
		mydb = myclient['audit']
		mycol = mydb['mobile_party']

		# 根据手机号查询
		myfix = {'mobile': mobile,"function" : "mobileOnline"}
		# 修改语句，将查询出的内容对应位置修改为c的内容
		new_values = {'$set':{"type" : mobileOnline_type}}
		mycol.update_many(myfix,new_values)
		
		# 打印修改后的结果
		for x in mycol.find(myfix):
				print('联系人手机号:%s 类型:%s from:%s 状态:%s\n' % (x['mobile'],x['function'],x['from'],x['type']))

if __name__ == '__main__':
	pass









