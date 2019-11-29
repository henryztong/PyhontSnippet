from functools import wraps
def a(func):

	print(1)
	print(func())
	# @wraps(func) #用于反重写函数名和注释文档 
	def b(): # 嵌套函数
		print(2)
		func()
		print(3)
	
	return b
# 说明0，转自https://www.runoob.com/w3cnote/python-func-decorators.html
@a
def c():
	print(4)
# 等价于
# def c():
# 	print(4)
# c = a(c) # 不带参数的函数传递，将对象b传给了c，@语法糖的作用就相当于这句话

print(c.__name__)
c() #这里相当于执行了函数b的结果



# 说明1
# k = c # 将一个函数赋值给一个变量
# k() # 变量调用函数，加()表示函数调用


# 说明2
# c() # 先执行了装饰的c()，
# print('---')
# print(a(c())) # 装饰的c()只执行了一次，在执行a()
# print('---')
# a(c())
# print('---')
# print(a(c()))


# 说明3
# 相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点

# 说明4，执行顺序：
# 1. 执行@a，打印1和返回对象b
# 2. 将b对象重新赋值给新c变量，这一步就代表了@方法的作用
# 3. 再执行c()方法时，才调用b()方法
# 转自：https://blog.csdn.net/by_side_with_sun/article/details/80573228
