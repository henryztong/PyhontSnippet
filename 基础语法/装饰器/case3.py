def a():
	def b():
		print(1)
	return b


print(a()) # 相当于执行a函数，获得b对象
a()() # 相当于执行b函数