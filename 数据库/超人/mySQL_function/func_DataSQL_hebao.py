# 临时解决模块导入问题办法
# import sys
# import os
# current_dir = os.path.dirname(__file__)
# print(current_dir)
# # parent_dir = os.path.abspath(os.path.join(current_dir,os.pardir))
# # # print(parent_dir)
# # parent_dir = os.path.abspath(os.path.join(parent_dir,os.pardir))
# # print(parent_dir)
# # sys.path.append(parent_dir)
# print(sys.path)

from sqlalchemy import Column, Integer, String, create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
from mySQL_function.hebao_model.sp_grant_credits import Credit
from mySQL_function.hebao_model.sp_grant_user_contacts import UserContact
from mySQL_function.hebao_model.sp_grant_credit_opr import CreditOpr
from mySQL_function.hebao_model.sp_grant_credit_user import CreditUser
from mySQL_function.hebao_model.sp_grant_credit_user_company import CreditUserCompany
from mySQL_function.hebao_model.sp_grant_credit_user_relation import CreditUserRelation
from mySQL_function.hebao_model.sp_grant_store import Store
from mySQL_function.hebao_model.sp_grant_user_photos import UserPhoto
from mySQL_function.func_DataSQL_basic import *
import mysql.connector


class DataSQL_hebao(object):
	"""该模块作用：获取和包自动审核所需要的字段 """
	# 连接数据库并实例化一个对象,格式：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'，sp_grant和包库，fqcr分期超人库
	engine = create_engine('mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/sp_grant')
	# engine = create_engine('mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/fqcr')
	# 创建session用来操作数据库	
	DBSession = sessionmaker(bind=engine)
	session  = DBSession()

	def writeinto_txt(self,apply_no):
		# 将所有模块需要的参数信息一次性写入文本
		print("调试用方法，不能直接调该方法，因为写入文件路径会有问题")

		# base_txt_url = "../data/autoCheck_data/base.txt" 
		# self.writeInto_base(apply_no,base_txt_url)

		# ConsumptionGrade_txt_url = "../data/autoCheck_data/ConsumptionGrade.txt" 
		# self.writeInto_ConsumptionGrade(apply_no,ConsumptionGrade_txt_url)

		# FaceRecognition_txt_url = "../data/autoCheck_data/FaceRecognition.txt" 
		# self.writeInto_FaceRecognition(apply_no,FaceRecognition_txt_url)

		# IdcardValidate_txt_url = "../data/autoCheck_data/IdcardValidate.txt" 
		# self.writeInto_IdcardValidate(apply_no,IdcardValidate_txt_url)

		# NetworkTime_txt_url = "../data/autoCheck_data/NetworkTime.txt" 
		# self.writeInto_NetworkTime(apply_no,NetworkTime_txt_url)

		# OnlineStatus_txt_url = "../data/autoCheck_data/OnlineStatus.txt" 
		# self.writeInto_OnlineStatus(apply_no,OnlineStatus_txt_url)

		# RepeatContacks_txt_url = "../data/autoCheck_data/RepeatContacks.txt" 
		# self.writeInto_RepeatContacks(apply_no,RepeatContacks_txt_url)

		# RepeatOrder_txt_url = "../data/autoCheck_data/RepeatOrder.txt" 
		# self.writeInto_RepeatOrder(apply_no,RepeatOrder_txt_url)

		# RiskControlA_txt_url = "../data/autoCheck_data/RiskControlA.txt" 
		# self.writeInto_RiskControlA(apply_no,RiskControlA_txt_url)

		# RiskControlB_txt_url = "../data/autoCheck_data/RiskControlB.txt" 
		# self.writeInto_RiskControlB(apply_no,RiskControlB_txt_url)


	def writeInto_base(self,apply_no,txt_url):
		# 该方法作用：将自动审核base模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/base.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核base模块需要的参数
		Credit_Base_list = ['apply_no','created']
		CreditUser_Base_list = ['idcard','mobile','idname','user_prov_no']
		CreditUserRelation_Base_list = ['bank_card_mobile']
		CreditOpr_Base_list = ['opr_id']
		CreditUserCompany_Base_list= ['provice']
		UserContact_Base_list = ['contact_name','contact_mobile','relation_ship']

		# 目前(2019-07-11),渠道为两个：11.和包，5.翼支付，请注意维护		
		dicts = {'channel':'11'}

		# 查询对应表中的数据
		# 注意：
		# Credit是模型名，即数据库表名，数据类型为对象，比如from object_model.sp_grant_credit_opr import CreditOpr中的CreditOpr
		# Credit.apply_no被查询的列名，列名为对象的属性，即字段名，比如Credit.apply_no
		# apply_no被查询的条件值，比如apply_no = 'tt20190717181650'
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)
		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)
		CreditOpr_list = DB_basic.two_table(Credit,Credit.id,CreditOpr,CreditOpr.id,Credit.apply_no,apply_no)
		UserContact_list = DB_basic.two_table(Credit,Credit.id,UserContact,UserContact.credit_id,Credit.apply_no,apply_no)

		CreditUserCompany_list = DB_basic.two_table(Credit,Credit.id,CreditUserCompany,CreditUserCompany.id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_Base_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_Base_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_Base_list,txt_url)
		self.query_filter(CreditOpr_list,CreditOpr_Base_list,txt_url)
		self.query_filter(UserContact_list,UserContact_Base_list,txt_url)
		self.query_filter(CreditUserCompany_list,CreditUserCompany_Base_list,txt_url)
		self.write_format(dicts,txt_url)

	def writeInto_ConsumptionGrade(self,apply_no,txt_url):
		# 该方法作用：将自动审核ConsumptionGrade模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/ConsumptionGrade.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核ConsumptionGrade模块需要的参数
		ConsumptionGrade_list = ['apply_no']

		# main_phone是在网状态模块后生成，非直接取MySQL数据库的值
		dicts = {'main_phone':''}
		

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,ConsumptionGrade_list,txt_url)
		self.write_format(dicts,txt_url)

	def writeInto_FaceRecognition(self,apply_no,txt_url):
		# 该方法作用：将自动审核FaceRecognition模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/FaceRecognition.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核FaceRecognition模块需要的参数
		FaceRecognition_list = ['apply_no','idcard_front_url','live_picture_url']

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)
		UserPhoto_list = DB_basic.two_table(Credit,Credit.id,UserPhoto,UserPhoto.credit_id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,FaceRecognition_list,txt_url)
		self.query_filter(UserPhoto_list,FaceRecognition_list,txt_url)

	def writeInto_IdcardValidate(self,apply_no,txt_url):
		# 该方法作用：将自动审核IdcardValidate模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/IdcardValidate.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核IdcardValidate模块需要的参数
		Credit_IdcardValidate_list = ['apply_no']
		CreditUser_IdcardValidate_list = ['idname','idcard','idcard_exp_edt','user_id']
		UserPhoto_IdcardValidate_list = ['idcard_front_url']

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)

		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		UserPhoto_list = DB_basic.two_table(Credit,Credit.id,UserPhoto,UserPhoto.credit_id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_IdcardValidate_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_IdcardValidate_list,txt_url)
		self.query_filter(UserPhoto_list,UserPhoto_IdcardValidate_list,txt_url)



	def writeInto_NetworkTime(self,apply_no,txt_url):
		# 该方法作用：将自动审核NetworkTime模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/NetworkTime.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核NetworkTime模块需要的参数
		Credit_NetworkTime_list = ['apply_no']
		CreditUser_NetworkTime_list = ['mobile','idname']
		CreditUserRelation_NetworkTime_list = ['bank_card_mobile']


		# 新库中没有这两个字段，是由之前模块传值过来的，所以默认设为空需要自定义
		dicts = {'selleCondition':'','refuseButAgree':''}

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)

		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_NetworkTime_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_NetworkTime_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_NetworkTime_list,txt_url)
		self.write_format(dicts,txt_url)


	def writeInto_OnlineStatus(self,apply_no,txt_url):
		# 该方法作用：将自动审核OnlineStatus模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/OnlineStatus.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核OnlineStatus模块需要的参数
		Credit_OnlineStatus_list = ['apply_no']
		CreditUser_OnlineStatus_list = ['idname']
		UserContact_OnlineStatus_list = ['contact_name','contact_mobile','relation_ship']
		# 目前(2019-07-11),渠道为两个：11.和包，5.翼支付，请注意维护
		dicts = {'channel':'11'}

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)
		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		UserContact_list = DB_basic.two_table(Credit,Credit.id,UserContact,UserContact.credit_id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_OnlineStatus_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_OnlineStatus_list,txt_url)
		self.query_filter(UserContact_list,UserContact_OnlineStatus_list,txt_url)
		self.write_format(dicts,txt_url)


	def writeInto_RepeatContacks(self,apply_no,txt_url):
		# 该方法作用：将自动审核RepeatContacks模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/RepeatContacks.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核RepeatContacks模块需要的参数
		Credit_RepeatContacks_list = ['apply_no']
		CreditUser_RepeatContacks_list = ['mobile','user_id']
		CreditUserRelation_RepeatContacks_list = ['bank_card_mobile']
		UserContact_RepeatContacks_list = ['contact_name','contact_mobile']
		# 是否优质商家，1为优质商家  
		dicts = {'selleCondition':''}

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)
		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)
		UserContact_list = DB_basic.two_table(Credit,Credit.id,UserContact,UserContact.credit_id,Credit.apply_no,apply_no)
		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_RepeatContacks_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_RepeatContacks_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_RepeatContacks_list,txt_url)
		self.query_filter(UserContact_list,UserContact_RepeatContacks_list,txt_url)
		self.write_format(dicts,txt_url)


	def writeInto_RepeatOrder(self,apply_no,txt_url):
		# 该方法作用：将自动审核RepeatOrder模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/RepeatOrder.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核RepeatOrder模块需要的参数
		Credit_RepeatOrder_list = ['apply_no']
		CreditUser_RepeatOrder_list = ['mobile','idcard']
		CreditUserRelation_RepeatOrder_list = ['bank_card_mobile']


		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)
		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)

		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_RepeatOrder_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_RepeatOrder_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_RepeatOrder_list,txt_url)


	def writeInto_RiskControlA(self,apply_no,txt_url):
		# 该方法作用：将自动审核RiskControlA模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/RiskControlA.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核RiskControlA模块需要的参数
		Credit_RiskControlA_list = ['apply_no']
		CreditUser_RiskControlA_list = ['idcard','idname','user_id','email']
		CreditUserRelation_RiskControlA_list = ['address','bank_card_no','bank_card_mobile','schooling','marital_sta']
		UserContact_RiskControlA_list = ['contact_name','contact_mobile','relation_ship']
		CreditOpr_RiskControlA_list = ['opr_id']
		CreditUser_company_RiskControlA_list = ['name','address']
		
		# 经度、纬度、主号码、城市地址、授信类型、白骑士规则
		dicts = {'longitude':'','latitude':'','main_phone':'','addressCity':'','credit_type':'','white_event_type':''}


		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)

		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)
		UserContact_list = DB_basic.two_table(Credit,Credit.id,UserContact,UserContact.credit_id,Credit.apply_no,apply_no)
		CreditOpr_list = DB_basic.two_table(Credit,Credit.id,CreditOpr,CreditOpr.id,Credit.apply_no,apply_no)
		CreditUserCompany_list = DB_basic.two_table(Credit,Credit.id,CreditUserCompany,CreditUserCompany.id,Credit.apply_no,apply_no)



		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_RiskControlA_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_RiskControlA_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_RiskControlA_list,txt_url)
		self.query_filter(UserContact_list,UserContact_RiskControlA_list,txt_url)
		self.query_filter(CreditOpr_list,CreditOpr_RiskControlA_list,txt_url)
		self.query_filter(CreditUserCompany_list,CreditUser_company_RiskControlA_list,txt_url)
		self.write_format(dicts,txt_url)

	def writeInto_RiskControlB(self,apply_no,txt_url):
		# 该方法作用：将自动审核RiskControlB模块需要的参数从数据库中查询出来写入到文本
		# txt_url 文本输出地址，txt_url = "../data/autoCheck_data/RiskControlB.txt" 
		# apply_no 被查询的流水号

		# 判断要输出的文档中是否已存在内容，存在则清除
		with open(txt_url,'w+',encoding='utf-8') as config:
			if config.read():
				pass
		
		# 自动审核RiskControlB模块需要的参数
		Credit_lRiskControlB_list = ['apply_no']
		CreditUser_RiskControlB_list = ['idcard','email','idname']
		CreditUserRelation_RiskControlB_list = ['address','marital_sta','schooling','bank_card_no','in_come']
		UserContact_RiskControlB_list = ['contact_name','contact_mobile','relation_ship']
		CreditUserCompany_RiskControlB_list = ['name','address','contact_mobile']

		# 经度、纬度、公司所属行业、在职状态、商户评级
		dicts = {'main_phone':'','longitude':'','latitude':'','company_industry':'','applyer_type':'','sellerAssess':''}

		# 查询对应表中的数据
		DB_basic= func_DataSQL_basic(session)
		Credit_list = DB_basic.one_table(Credit,Credit.apply_no,apply_no)

		CreditUser_list = DB_basic.two_table(Credit,Credit.id,CreditUser,CreditUser.id,Credit.apply_no,apply_no)
		CreditUserRelation_list = DB_basic.two_table(Credit,Credit.id,CreditUserRelation,CreditUserRelation.id,Credit.apply_no,apply_no)
		CreditOpr_list = DB_basic.two_table(Credit,Credit.id,CreditOpr,CreditOpr.id,Credit.apply_no,apply_no)
		UserContact_list = DB_basic.two_table(Credit,Credit.id,UserContact,UserContact.credit_id,Credit.apply_no,apply_no)
		CreditUserCompany_list = DB_basic.two_table(Credit,Credit.id,CreditUserCompany,CreditUserCompany.id,Credit.apply_no,apply_no)


		# 筛选后写入文本
		self.query_filter(Credit_list,Credit_lRiskControlB_list,txt_url)
		self.query_filter(CreditUser_list,CreditUser_RiskControlB_list,txt_url)
		self.query_filter(CreditUserRelation_list,CreditUserRelation_RiskControlB_list,txt_url)
		self.query_filter(UserContact_list,UserContact_RiskControlB_list,txt_url)
		self.query_filter(CreditUserCompany_list,CreditUserCompany_RiskControlB_list,txt_url)
		self.write_format(dicts,txt_url)


	def write_format(self,read_dict,txt_url):
		# 该方法作用：按照一定格式写入到文本		
		# txt_url 文本输出地址，txt_url = "./input_parameter1.txt"
		# read_dict读取要写入的值

		string = ''	
		config =open(txt_url,'a+',encoding="utf-8")# a+表示在文本结尾继续写入内容
		# print(read)
		for x in read_dict:
			string = x+':'+str(read_dict[x])+'\n'
			# print(string)	
			config.write(string)
		config.close()


	def query_filter(self,query_list,key_list,txt_url,table_name=''):		
		# 该方法作用：从查询到的结果中筛选出对应的字段的值，以一定格式写入文本		
		# query_list数据库查询结果
		# key_list要筛选的字段名列表
		# table_name是加的备注信息，以便区分不同表字段名相同，调试用可不加
		# txt_url 文本输出地址

		for dict_data in query_list:	
			# 该表达式作用等于下面的for语句
			dicts = {x:dict_data[x] for x in key_list if x in dict_data} 
			# dicts = {}
			# for x in key_list:
			# 	# print(x)
			# 	if x in dict_data:
			# 		# print(x)
			# 		# print(dict_data[x])
			# 		key =table_name+x
			# 		dicts[key]=dict_data[x]
			# print(dicts)
			self.write_format(dicts,txt_url)
		return 	dicts	

	def updates(self):
		pass



if __name__ == '__main__':
	apply_no = 'tt20190717181650'
	txt_url = "../data/autoCheck_data/RiskControlB.txt"
	a = DataSQL_hebao()

	# a.writeInto_RiskControlB(apply_no,txt_url)
	# a.writeinto_txt(apply_no)

