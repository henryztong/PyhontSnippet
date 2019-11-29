
# 读取txt文件转json操作
class input_data(object):
	"""读取txt文档操作"""
	def get_data(self,path):
		web_info = {}
		with open(path,'r',encoding="utf-8") as config:
			for line in config:
		 	# 将获取的数据使用=号分割,并将空格去掉
				result = [ele.strip() for ele in line.split(':')]
			# 将列表转化为字典(字典不是有序的)，并添加到webinfo中
				web_info.update(dict([result])) 
		return web_info

if __name__ == '__main__':
	path = './hebao_param.txt'
	a = input_data()
	b = a.get_data(path)
	print(b)
	print(type(b))