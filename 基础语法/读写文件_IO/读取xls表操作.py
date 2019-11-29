# 读取xls表操作

import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir,os.pardir))
sys.path.append(parent_dir)
print(sys.path)
import requests
import json
import datetime
import mysql.connector
import xlrd
import codecs
from data.parameter import Grantapplyservice
# 翼支付授信接口获取输入参数模块


class XLUserinfo(object):
	"""读取Excel表操作"""
	def __init__(self,path = ''):
		self.xl = xlrd.open_workbook(path) #打开excel文件，并将其赋给一个对象xl

	def floattostr(self,val): 
		# 浮点型数据转换为字符串
		if isinstance(val,float): 
			val = str(int(val))
		return val

	def get_sheet_info(self): 
	# 得到某张表中的所有数据
		listkey = ['key','value']
		infolist = []
		for row in range(1,self.sheet.nrows): # 根据行数进行遍历,从第二行开始
			info = [ self.floattostr(val) for val in self.sheet.row_values(row)] 
			# 获取某一行数据，返回的是列表类型。并对里面的数字类型数据进行解析
			# info = self.sheet.row_values(row) # 获取的数值类型是浮点型的，需要转化为字符串
			# tmp = zip(listkey,info) # 将列表的2个值打包为元组对象
			# infolist.append(dict(tmp)) # 将元组数据转换为字典并添加到新列表中
			templist = []
			for i in range(0,2):  # 只取两列，第一列和第二列
				templist.append(info[i])
			infolist.append(templist)
		dict1 = dict(infolist) # 将列表转换为字典格式
		# print(dict1)
		return dict1

	def get_sheetinfo_by_name(self,name): #通过名字获取表
		self.sheet = self.xl.sheet_by_name(name)  # 修改了xl.sheet方法使其根据表名获取表
		return self.get_sheet_info() #获取表中数据，并返回获取的数据

	def get_sheetinfo_by_index(self,index): #通过索引获取表
		self.sheet = self.xl.sheet_by_index(index)
		return self.get_sheet_info()

class Placeorder(object):
	"""以xls中的数据为参数进行授信接口请求，常用"""
	def __init__(self):
		super(Placeorder, self).__init__()
	def req(self):
		# 根据XLUserinfo中的get_sheetinfo_by_index方法获取Excel中数据
		open_data = XLUserinfo(parameter)
		# 读取测试数据
		payload = open_data.get_sheetinfo_by_index(0)
		# print(type(payload))
		# print(payload)
		# 随机生成时间戳替换Excel中的applyNo
		time = datetime.datetime.now()
		time2 = datetime.datetime.strftime(time,'%Y%m%d%H%M%S')
		payload["applyNo"] = time2
		applyNo = payload['applyNo']
		print('手机号= ',payload['mobileNo'])
		# 发送请求
		r = requests.post(url,data=payload)
		a = json.loads(r.text)
		print(a)
		# print(type(payload['photoInfo']))
		# print(type(payload['contacts']))
		# print(payload['contacts'])
		return applyNo

class Placeorder2(object):
	"""以parameter.py中的数据为参数进行授信接口请求"""
	def __init__(self):
		super(Placeorder2, self).__init__()

	def para2(self):
		dic = Para()
		payload = dic.para()
		applyNo = payload['applyNo']
		print(type(payload['contacts']))
		print(payload['photoInfo'])
		print(payload['contacts'])
		r = requests.post(url,data=payload)
		a = json.loads(r.text)
		print(a)
		return applyNo

class Photo_XLUserinfo(object):
	"""获取excel中存的图片地址信息"""
	def __init__(self,path = ''):
		self.xl = xlrd.open_workbook(path) #打开excel文件，并将其赋给一个对象xl

	def floattostr(self,val): 
		if isinstance(val,float): # 如果传入的值是浮点型的话就需要转换
			val = str(int(val))
		return val

	def get_sheet_info(self): # 得到某张表中的所有数据
		listkey = ['key','value']
		infolist = []
		for row in range(1,4): # 只取前3行,从第二行开始
			info = [ self.floattostr(val) for val in self.sheet.row_values(row)] 
			templist = []
			for i in range(3,5):  # 第4列和第5列,只取了2列，不然转字典要报错
				templist.append(info[i])
			infolist.append(templist)
		dict1 = dict(infolist) # 将列表转换为字典格式
		# print(dict1)
		return dict1

	def get_sheetinfo_by_name(self,name): #通过名字获取表
		self.sheet = self.xl.sheet_by_name(name)  # 修改了xl.sheet方法使其根据表名获取表
		return self.get_sheet_info() #获取表中数据，并返回获取的数据

	def get_sheetinfo_by_index(self,index): #通过索引获取表
		self.sheet = self.xl.sheet_by_index(index)
		return self.get_sheet_info()

class Insert(object):
	"""将图片地址photo_url插入数据库"""
	def __init__(self):
		super(Insert, self).__init__()

	def insertphoto(self):
		# 根据Photo_XLUserinfo中的get_sheetinfo_by_index方法获取Excel中数据
		xinfo = Photo_XLUserinfo(parameter)
		info = xinfo.get_sheetinfo_by_index(0)
		# 打开数据库
		cnx = mysql.connector.connect(user='sp_man',password='Spman@123#admin.com',host='119.23.145.20',database='fqcr')
		# 开启游标
		cursor = cnx.cursor()
		# 修改已存入photo_id的photo_url值
		for key in info:	
			photo_url = info[key]
			photo_id = key
			# print(photo_url,photo_id)
			query = ('update user_photo_yi set photo_url=%s' 'where photo_id=%s')
			data = (photo_url,photo_id)
			cursor.execute(query,data)
		cnx.commit()
		cursor.close()
		cnx.close()
		return "图片信息已导入user_photo_yi表"


if __name__ == '__main__':
	url = "http://api.test.fenqichaoren.com/yipay"
	# url = "http://api.beta.fenqichaoren.com/yipay"
	# url = "http://api.fenqichaoren.com/yipay"
	parameter = r'../data/userinfo-test.xls'
	parameter = r'../data/userinfo-beta.xls'
	r = Placeorder()
	a = r.req()
	print(a)
	# r2 = Placeorder2()
	# b = r2.para2()
	# print(b)
	# a = Insert()
	# b = a.insertphoto()
	# print(b)
	# pass













