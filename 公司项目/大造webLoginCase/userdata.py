# coding=utf-8
import codecs
import xlrd
# 读取文本中的方法
def get_webinfo(path): # 获取元素数据
	web_info = {}
	# config = open(path)  # 读取文件方法1，并将每行以列表的形式返回，这时返回的数据中有\n
	config = codecs.open(path,'r') # 读取方法2，‘r’表示读取，可修改编码格式
	
	for line in config:
		result = [ele.strip() for ele in line.split('=')]  # 将获取的数据使用=号分割,并将空格去掉
		web_info.update(dict([result])) # 将列表转化为字典(字典不是有序的)，并添加到webinfo中
	return web_info

def get_userinfo(path): # 获取用户数据
	user_info=[]
	config = codecs.open(path,'r')
	for line in config:
		result = [ele.strip() for ele in line.split(';')] # 根据空格将每行进行分割
		# print(result)
		user_dict = {}
		for r in result:
			account = [ele.strip() for ele in r.split('=')] # 根据等号将字符串进行分割
			user_dict.update(dict([account]))
		user_info.append(user_dict)
	return user_info

class XLUserinfo(object):
	"""docstring for XLUserinfo"""
	def __init__(self,path = ''):
		self.xl = xlrd.open_workbook(path) #打开excel文件，并将其赋给一个对象xl

	def floattostr(self,val): 
		if isinstance(val,float): # 如果传入的值是浮点型的话就需要转换
			val = str(int(val))
		return val

	def get_sheet_info(self): # 得到某张表中的所有数据
		listkey = ['uname','pwd']
		infolist = []
		for row in range(1,self.sheet.nrows): # 根据行数进行遍历
			info = [ self.floattostr(val) for val in self.sheet.row_values(row)] # 获取某一行数据，返回的是列表类型。并对里面的数字类型数据进行解析
			# info = self.sheet.row_values(row) # 获取的数值类型是浮点型的，需要转化为字符串
			tmp = zip(listkey,info) # 将2个列表打包为元组
			# print(tmp)
			infolist.append(dict(tmp)) # 将元组数据转换为字典并添加到列表中
			# print(infolist)
		return infolist

	def get_sheetinfo_by_name(self,name): #通过名字获取表
		self.sheet = self.xl.sheet_by_name(name)  # 修改了xl.sheet方法使其根据表名获取表
		return self.get_sheet_info() #获取表中数据，并返回获取的数据

	def get_sheetinfo_by_index(self,index): #通过索引获取表
		self.sheet = self.xl.sheet_by_index(index)
		return self.get_sheet_info()
		
#
# if __name__ == '__main__':
	# info = get_webinfo(r'G:\case\webinfo.txt')
	# info2 = get_userinfo(r'G:\case\userinfo.txt')
	# # for key in info2:
	# # 	print(key) # 查看user_info列表中的字典
	# print(info2) # 查看user_info列表

	# xinfo = XLUserinfo(r'G:\case\userinfo.xls')
	# info = xinfo.get_sheetinfo_by_index(0)
	# print(info)

	# info2 = xinfo.get_sheetinfo_by_name('Sheet1')
	# print(info2)
	# psss


