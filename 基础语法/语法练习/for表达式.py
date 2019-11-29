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