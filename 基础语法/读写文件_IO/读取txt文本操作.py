import codecs

# 读取txt文件转json操作
class input_data(object):
	"""
	读取txt文档操作
	codecs进行文件的读取
	python给我们提供了一个包codecs进行文件的读取，这个包中的open()函数可以指定编码的类型：
	"""
	def get_data(self,path): # 获取元素数据
		web_info = {}
		# config = open(path)  # 读取文件方法1，并将每行以列表的形式返回，这时返回的数据中有\n
		# config = codecs.open(path,'r') # 读取方法2，‘r’表示读取，可修改编码格式

		# with open(path,'r') as f:
			# config= f.readline()
			# config = bytes.decode(config)
			# print(config)
			# print(type(config))
			# for line in f:
				# print(line, end='')
				
		# print(config)
		# print(type(config))

		# with open(path,'r') as config:
		# 	print(config)
		# 	print(config.read())
		config = open(path,'r',encoding="utf-8")
		for line in config:
			print(line)
			print(type(line))
	 	# 将获取的数据使用=号分割,并将空格去掉
			result = [ele.strip() for ele in line.split(':')]
		# 	print(dict([result]))
		# 	# 将列表转化为字典(字典不是有序的)，并添加到webinfo中
			web_info.update(dict([result])) 
		
		return web_info

	def get_data2(self,path):
		web_info = {}
		with open(path,'r',encoding="utf-8") as config:
			for line in config:
				print(line)
				print(type(line))
		 	# 将获取的数据使用=号分割,并将空格去掉
				result = [ele.strip() for ele in line.split(':')]
			# 将列表转化为字典(字典不是有序的)，并添加到webinfo中
				web_info.update(dict([result])) 
		return web_info

	def readFrom_txt(self,txt_url):
		# 读取文本中的值
		with open(txt_url,'r',encoding='utf-8') as f: 
			content = f.read()
		return content

if __name__ == '__main__':
	path = './hebao_param.txt'
	a = input_data()
	b = a.get_data2(path)
	print(b)
	# print(type(b))