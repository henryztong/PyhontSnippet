# coding=utf-8
import mysql.connector
import json
import datetime
# MySQL数据库操作模块
# func_DataSQL.py

class func_DataSQL(object):
	"""数据库操作"""
	def __init__(self):
		super(func_DataSQL, self).__init__()

	def connect_mysql(self):
		# 连接测试数据库
		cnx = mysql.connector.connect(user='sp_man',password='Spman@123#admin.com',host='119.23.145.20',database='fqcr')
		# 连接正式只读数据库
		# cnx = mysql.connector.connect(user='tangyupeng',password='zKv8JH!M50Nt',host='rds1s112jte2w7eq6b2ro.mysql.rds.aliyuncs.com',database='fqcr')	
		return cnx

	def select_mysql(self,sql,value):
		# 查询方法
		cnx = self.connect_mysql()
		cursor = cnx.cursor()	# 开启游标 
		cursor.execute(sql,value) 	  # 执行sql语句，sql变量为查询语句,value为元组类型
		result = cursor.fetchall() # 获取查询结果
		cnx.commit() 		# 提交sql语句
		cursor.close() 		# 关闭游标
		cnx.close() 		# 关闭数据库连接
		# 由于查询结果为元组类型，所以要将查询的结果转化为列表，以便在写入时转换为字典
		list_result = self.toList(result)
		return list_result

	def update_mysql(self,sql,value):
		# 修改数据库操作
		cursor = self.connect_mysql()	# 连接数据
		cursor.execute(sql,value) 	  # 执行sql语句，sql变量为查询语句,value为元组类型
		cnx.commit() 		# 提交sql语句
		cursor.close() 		# 关闭游标
		cnx.close() 		# 关闭数据库连接
		print('修改数据成功')

	def add_mysql(self,sql,value):
		# 新增操作
		cnx = self.connect_mysql()	# 连接数据
		cursor = cnx.cursor()	# 开启游标 
		cursor.execute(sql,value) 	  # 执行sql语句，sql变量为修改语句,字符串类型,value为元组类型
		cnx.commit() 		# 提交sql语句
		cursor.close() 		# 关闭游标
		cnx.close() 		# 关闭数据库连接
		print('新增数据成功')

	def toList(self,tuple_value):		
		# 将元祖类型转化为列表类型
		# 初始化一个列表用来存放查询结果，返回列表值
		list_value = []
		# 将元组转换为列表
		for x in range(0,len(tuple_value)):
			for j in range(0,len(tuple_value[x])):
				# print(tuple_value[x][j])
				list_value.append(tuple_value[x][j])
		return list_value

	def get_list_key(self):
		# 定义列表，该列表的值作为字典中的key
		user_extend_yi_key = ['apply_no','phone','bank_mobile_no','create_time','user_name','seller_main_id','id_number','id_validity_end','user_main_id','residence_address','is_married','company_name','company_address','bank_no','longitude','latitude','education','industry_type','salary','seller_province']
		user_photo_yi_key = ['facePicUrl','backPicUrl','portraitsPicUrl']
		user_linkman_yi_key = ['mobile1','contact_name1','contact_relation_ship1','mobile2','contact_name2','contact_relation_ship2']
		list_key = user_extend_yi_key + user_photo_yi_key + user_linkman_yi_key
		return list_key

	def get_list_value(self,apply_no):
		# 定义列表，该列表的值作为字典中的value
		value = (apply_no,)
		# 查询user_extend_yi
		user_extend_yi_sql = ('select e.apply_no,e.phone,e.bank_mobile_no,e.create_time,e.user_name,e.seller_main_id,e.id_number,e.id_validity_end,e.user_main_id,e.residence_address,e.is_married,e.company_name,e.company_address,e.bank_no,e.longitude,e.latitude,e.education,e.industry_type,e.salary,e.seller_province from user_extend_yi e where e.apply_no = %s')

		# 查询user_photo_yi		
		user_photo_yi_sql = ('select distinct p.photo_url from user_extend_yi e left join user_photo_yi p on p.user_extend_yi_id = e.id where e.apply_no = %s and photo_type in (7,8,15)' )

		# 查询user_linkman_yi
		user_linkman_yi_sql = ('select l.contact_mobile,l.contact_name,l.contact_relation_ship from user_extend_yi e left join user_linkman_yi l on l.user_main_id = e.user_main_id  where e.apply_no = %s')


		# 将查询后的结果进行拼接
		user_extend_yi_re = self.select_mysql(user_extend_yi_sql,value)
		user_photo_yi_re = self.select_mysql(user_photo_yi_sql,value)
		user_linkman_yi_re  = self.select_mysql(user_linkman_yi_sql,value)
		# print(user_photo_yi_re)
		# print(len(user_photo_yi_re))
		# print(user_photo_yi_re[0])
		# print(type(user_photo_yi_re[0]))
		# 由于正式环境进单后不能修改数据库数据，无法存入图片地址，获取到的数据为None需要转换为null
		if len(user_photo_yi_re):	
			if user_photo_yi_re[0] :
				for x in range(0,3):
					user_photo_yi_re[x] = 'http://fqcr.oss-cn-shenzhen.aliyuncs.com/' + user_photo_yi_re[x]
			else:
				user_photo_yi_re.clear()
				for x in range(0,3):
					user_photo_yi_re.append('null')
		else:
			for x in range(0,3):
				user_photo_yi_re.append('null')

		# print(user_photo_yi_re)
		# 拼接值
		list_value = user_extend_yi_re + user_photo_yi_re + user_linkman_yi_re
		# print(list_value)
		return list_value


	def writeInto_txt(self,list_key,list_value,write_url):
		# 将查询出的数据保存到文件中

		# 将两个列表转换一个字典
		select_result = dict(zip(list_key,list_value)) 
		# print(select_result)

		# 将字典转换为字符串输出
		result = json.dumps(select_result) 

		# 在macOS中python3必须以encoding='utf-8'格式打开文件再读写
		with open(write_url,'w',encoding='utf-8') as f: 
			f.write(result)
		print('参数已写入%s' % (write_url))

	def readFrom_txt(self,read_url):
		# 读取文本中的值
		with open(read_url,'r',encoding='utf-8') as f: 
			content = f.read()
		return content


if __name__ == '__main__':
	# 在本文件中直接调试
	apply_no = '20190320081442' #调试
	txt_url = "./input_parameter1.txt" #调试

	a = func_DataSQL()
	list_key = a.get_list_key() # 该列表的值作为字典中的key
	list_value = a.get_list_value(apply_no) # 该列表的值作为字典中的value
	# print(list_key)
	# print(list_value)

	a.writeInto_txt(list_key,list_value,txt_url)
	# c = a.readFrom_txt(txt_url)
	# print(c)







