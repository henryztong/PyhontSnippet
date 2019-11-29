https://www.zhihu.com/question/27376156


在Python2.6以下版本字典生成器可以接受迭代的键值对:
d = dict((key, value) for (key, value) in iterable)

从Python2.7或者Python3以后,你可以直接用字典推导式语法:
d = {key: value for (key, value) in iterable}

你也可以用任何方式的迭代器(元组,列表,生成器..)，只要可迭代对象的元素中有两个值，
d = {value: foo(value) for value in sequence if bar(value)}



{k:v for k,v in a.items() if b in t} 
推导过程：
# -*- coding:utf-8 -*-
a={'a': '0', 'b': '1', 'c': '2', 'd':'3'}
t=a.keys()
b='a'
print {k:v for k,v in a.items() if b in t} #输出1
  
temp={}
for k,v in a.items():
    if b in t:
        temp[k]=v
print temp #输出2


---


{x:dict_data[x] for x in sift_data if x in dict_data}
等价于
for x in sift_data:
	# print(x)
	if x in dict_data:
		print(x) 
		print(dict_data[x])
		# key =key_table+x
		# dict1[key]=dict_data[x]
		dict1[x]=dict_data[x]
示例：
	def writeInto_txt(self,apply_no):
		# 将查询出的数据保存到文本中
		sift_data = ['apply_no','created','mobile','idname','idcard','idcard_exp_sdt','idcard_exp_edt','user_id','bank_card_mobile','address','marital_sta','bank_card_no','schooling','user_job','in_come','province','city','nation','store_id','name','address','city','contact_name','contact_mobile','relation_ship']

		UserContact_data = self.UserContact_data(apply_no)
		UserPhoto_data = self.UserPhoto_data(apply_no)
		Store_data = self.Store_data(apply_no)
		Credit_data = self.Credit_data(apply_no)
		CreditUser_data = self.CreditUser_data(apply_no)
		CreditUserRelation_data = self.CreditUserRelation_data(apply_no)
		CreditUserCompany_data = self.CreditUserCompany_data(apply_no)
		CreditOpr_data = self.CreditOpr_data(apply_no)

		list_data = Credit_data

		dict1 = {}
		for dict_data in list_data:
			print(dict_data)
			dict1 = {x:dict_data[x] for x in sift_data if x in dict_data}
			# for x in sift_data:
			# 	# print(x)
			# 	if x in dict_data:
			# 		print(x) 
			# 		print(dict_data[x])
			# 		dict1[x]=dict_data[x]
					
		print(dict1)

# 多个查询结果时

	def to_dict(self,list_data,key_list,key_table):
		list2 = []
		for dict_data in list_data:	
			if len(list_data)>1:
				a = self.filter(dict_data,key_list,key_table)
				list2.append(a)		
			else:
				list2 = self.filter(dict_data,key_list,key_table)

		print(list2)
		return list2

