from sqlalchemy import Column, Integer, String, create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
from mySQL_function.hebao_model.sp_grant_credits import Credit
from mySQL_function.bestpay_model.fqcr_user_extend_yi import UserExtendYi
from mySQL_function.bestpay_model.fqcr_user_photo_yi import UserPhotoYi
import mysql.connector


class func_DataSQL_basic(object):
	"""数据库基础操作 """

	def __init__(self,session):
		self.session  = session

# 查询3张表
	def three_table(self,table1_name,table1_column,table2_name,table2_column1,table2_column2,table3_name,table3_column,terms_column,column):
		# table_name1被查询的表名，右表
		# table_column1被查询的列名
		# table_name2被查询的表名，左表
		# table_column2被查询的列名
		# table_name3被查询的表名，左表
		# table_column3被查询的列名
		# terms_column以某个字段为查询条件
		# column被查询的条件值	

		query_result = self.session.query(table3_name).join(table2_name,table2_column2 == table3_column).join(table1_name,table1_column == table2_column1).filter(terms_column==column).all()
		result = Store.to_json(query_result)
		# print(result)
		return result

# 查询2张表
	def two_table(self,table1_name,table1_column,table2_name,table2_column,terms_column,column):
		# table_name1被查询的表名，右表
		# table_column1被查询的列名
		# table_name2被查询的表名，左表
		# table_column2被查询的列名
		# terms_column以某个字段为查询条件
		# column被查询的条件值
		# 左连接查询，查询满足右表字段值的所有左表数据	

		query_result = self.session.query(table2_name).join(table1_name,table1_column == table2_column).filter(terms_column==column).all()	
		result = table2_name.to_json(query_result)
		# print(result)
		return result

# 查询单表
	def one_table(self,table_name,terms_column,column):	
		# table_name被查询的表名，该表明传的是模型名，数据类型为对象，比如from object_model.sp_grant_credit_opr import CreditOpr中的CreditOpr
		# table_column被查询的列名，列名为对象的属性，比如Credit.apply_no
		# column被查询的条件值，比如apply_no = 'tt20190717181650'

		query_result = self.session.query(table_name).filter(terms_column==column).all()
		result = table_name.to_json(query_result)
		# print(result)
		return result

	def update_value (self,table_name,terms_column,column,terms_column2,column2):
		# 修改数据
		self.session.query(table_name).filter(terms_column==column).update({terms_column2:column2})
		self.session.commit()



# # 该方法作用：将查询出的数据保存到文本中
# 	def writeInto_txt(self,apply_no,txt_url,filter_list):
# 		# txt_url 文本输出地址，txt_url = "./input_parameter1.txt" 
# 		# apply_no 被查询的流水号
# 		# filter_list要查询的字段列表

# 		# 判断要输出的文档中是否已存在内容，存在则清除
# 		with open(txt_url,'w+',encoding='utf-8') as config:
# 			if config.read():
# 				pass
# 		Credit_list = self.one_table(Credit,Credit.apply_no,apply_no)


# 		# 筛选操作
# 		self.query_filter(Credit_list,filter_list,'Credit表字段：',txt_url)
# 		# self.query_filter(CreditUser_list,filter_list,'CreditUser表字段：',txt_url)
# 		# self.query_filter(CreditUserRelation_list,filter_list,'CreditUserRelation表字段：',txt_url)
# 		# self.query_filter(CreditUserCompany_list,filter_list,'CreditUserCompany表字段：',txt_url)
# 		# self.query_filter(CreditOpr_list,filter_list,'CreditOpr表字段：',txt_url)
# 		# self.query_filter(UserContact_list,filter_list,'UserContact表字段：',txt_url)
# 		# self.query_filter(UserPhoto_list,filter_list,'UserPhoto表字段：',txt_url)
# 		# self.query_filter(Store_list,filter_list,'Store表字段：',txt_url)

# # 该方法作用：按照一定格式写入到文本
# 	def write_format(self,read_data,txt_url):
		
# 		# txt_url 文本输出地址，txt_url = "./input_parameter1.txt"
# 		# read_data读取要写入的值

# 		string = ''	
# 		config =open(txt_url,'a+',encoding="utf-8")# a+表示在文本结尾继续写入内容
# 		# print(read)
# 		for x in read_data:
# 			string = x+':'+str(read_data[x])+'\n'
# 			# print(string)	
# 			config.write(string)
# 		config.close()

# # 该方法作用：从查询到的结果中筛选出对应的字段的值，以一定格式写入文本
# 	def query_filter(self,query_list,key_list,table_name,txt_url):		
		
# 		# query_list数据库查询结果
# 		# key_list要筛选的字段名
# 		# table_name是加的备注信息，以便区分不同表字段名相同
# 		# txt_url 文本输出地址

# 		# 作用等于下面的for语句
# 		# dicts = {x:dict_data[x] for x in key_list if x in dict_data} 
# 		dicts = {}
# 		for dict_data in query_list:	
# 			for x in key_list:
# 				# print(x)
# 				if x in dict_data:
# 					# print(x)
# 					# print(dict_data[x])
# 					key =table_name+x
# 					dicts[key]=dict_data[x]
# 			# print(dicts)
# 			self.write_format(dicts,txt_url)
# 		return 	dicts	

if __name__ == '__main__':
	apply_no = 'tt20190717181650'
	txt_url = "./input_parameter1.txt"
	# 连接数据库并实例化一个对象,格式：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'，sp_grant和包库，fqcr分期超人库
	# engine = create_engine('mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/sp_grant')
	engine = create_engine('mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/fqcr')
	# 创建session用来操作数据库	
	DBSession = sessionmaker(bind=engine)
	session  = DBSession()
	# 列出要查询的字段
	filter_list = ['apply_no','created','mobile','idname','idcard','idcard_exp_sdt','idcard_exp_edt','user_id','bank_card_mobile','address','marital_sta','bank_card_no','schooling','user_job','in_come','province','city','nation','store_id','name','address','city','contact_name','contact_mobile','relation_ship']
	# 注意：
	# table_name被查询的表名，该表明传的是模型名，数据类型为对象，比如from object_model.sp_grant_credit_opr import CreditOpr中的CreditOpr
	# table_column被查询的列名，列名为对象的属性，比如Credit.apply_no
	# column被查询的条件值，比如apply_no = 'tt20190717181650'
	# table1_name = Credit
	# table1_column = Credit.id
	# terms_column = Credit.apply_no

	a = func_DataSQL_basic(session)
	# data = a.UserContact_data(apply_no)
	# data = a.UserPhoto_data(apply_no)
	# data = a.Store_data(apply_no)
	# data = a.Credit_data(apply_no)
	# data = a.CreditUser_data(apply_no)
	# data = a.CreditUserRelation_data(apply_no)
	# data = a.CreditUserCompany_data(apply_no)
	# data = a.CreditOpr_data(apply_no)

	# data = a.one_table(table1_name,terms_column,apply_no)
	# data = a.two_table(table1_name,table1_column,table2_name,table2_column,terms_column,apply_no)
	# data = a.two_table(UserExtendYi,UserExtendYi.id,UserPhotoYi,UserPhotoYi.user_extend_yi_id,UserExtendYi.apply_no,apply_no)
	# print(data)
	# data = a.three_table(table1_name,table1_column,table2_name,table2_column1,table2_column2,table3_name,table3_column,terms_column,apply_no)
		# 201809271040537001	201906/201906250956526887.jpg	身份证正面
		# 201809271040537002	201906/20190625095652919.jpg	身份证反面
		# 201809271040537003	201906/201906250956525399.jpg	手持身份证
	data =a.update_value (UserPhotoYi,UserPhotoYi.photo_id,'201809271040537001',UserPhotoYi.photo_url,'201906/201906250956526887.jpg')
	# data =a.update_value (UserPhotoYi,UserPhotoYi.photo_id,'201809271040537002',UserPhotoYi.photo_url,'201906/20190625095652919.jpg')
	# data =a.update_value (UserPhotoYi,UserPhotoYi.photo_id,'201809271040537003',UserPhotoYi.photo_url,'201906/201906250956525399.jpg')


	# data =a.update_value (Credit,Credit.apply_no,'testTYP20190905105518',Credit.status,'0',Credit.audit_status,'0')

	# print(data)
	# print(len(data))
	# print(type(data))

	# a.writeInto_txt(apply_no,txt_url,filter_list)

