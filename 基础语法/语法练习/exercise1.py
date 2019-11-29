# coding:utf-8
# import keyword
# a = keyword.kwlist
# # print(a)
# print("123\n123")
# b = 'abc','def'
# print(b)

# str='good'
# print(str)
# print(str[0:-1])
# print(str[0])
# print(str[1:3])
# print(str[1:])
# print(str * 3)
# print(str + 'world')

# import sys;x='runoob';sys.stdout.write(x)
# from __future__ import print_function
# x='a'
# y='b'
# print(x,end='')
# print(y)
# import sys
# print('命令行参数')
# for i in sys.argv:
# 	print('文件地址：'+i)

# sys = str(sys.path)
# print('\n路径为 \n' +sys)



# a,b,c=1,2,3
# a = 10/3
# # sys.stdout.write(a)
# print(a)
# print(type(a))


# a=dict([('Runoob',1),('google',2)])
# print(a)

# a,b=10,20
# print(a and b)
# print(a or b)

# a=[1,2,3]
# print(a[:])


# a = 20
# b = 10
# c = 15
# d = 5
# e = 0

# e = (a + b) * c / d
# print('结果为 ',e)



# 
# while 1 : print('hello!')



# languages = ['C',"C++",'Perl','Python']
# a = (1,2,'aa','bb')
# for i in a:
# 	print(a[0])



# sites = ['baidu','google','runoob','taobao']
# for site in sites:
# 	if site == 'runoob':
# 		print('找到了runoob')
# 		# breakupper()
# 	print('循环数据' + site)
# else:
# 	print('没有数据')
# print('完成循环')

# import sys

# list=[1,2,3,4]
# it = iter(list)
# # for x in it:
# # 	print(1)


# while 1 :
# 	try:
# 		print(next(it))
# 	except Exception as e:
# 		sys.exit()

# def a():
# 	print('a')

# a()

# def area(width,height):
# 	return width * height

# def print_welcome(name):
# 	print('Welcome',name)

# print_welcome('henryztong')
# w = 10
# h = 5
# print('面积是 ',area(w,h))


# def changeme(mylist):
# 	mylist.append([1,2,3]);
# 	print('函数内的值: ',mylist)
# 	return
# mylist=[10,20,30]
# changeme(mylist)
# print('函数外取值: ',mylist)


# def ChangeInt(a):
# 	print('函数内的值a1：', a)
# 	a = 10
# 	print('函数内的值a：', a)
# 	print('函数内的值b：', b)

# b=2
# ChangeInt(b)
# print('函数外取值：',b)	


# def printinfo(arg1,*vartuple):
# 	print('输出：')
# 	print(arg1)
# 	for var in vartuple:
# 		print(var)
# 	return
# printinfo(11)
# printinfo(11,12,13,14)

# def sum(arg1,arg2):
# 	total= arg1 + arg2
# 	print('函数内的值：',total)
# 	return total
# total =sum(10,20)
# print('函数外取值：',total)


# num = 1
# def fun1():
# 	global num
# 	print(num)
# 	num = 123
# 	print(num)
# fun1()
# print(num)



# def local1():
# 	num = 10
# 	print(num)
# 	def inner():		
# 		nonlocal num
# 		num = 9
# 		print(num)
# 	inner()
# 	print(num)
# local1()


# a = 10
# def test(q,*a):
# 	print(q)
# 	print(a)
# test('l','3','ppp')

# sum = lambda lambda1,lambda2: lambda1 * lambda2
# print(sum(2,5))


# a = 10
# def test(a):
# 	a = a+1
# 	print(a)
# test(a)




# # x = input("你好")
# x = '你好'
# print('Henry %c' %(66))

# y = '''a \v 
# ?
# b'''
# print(y)

# Fibonacci series:斐波那契数列
# def FibonacciSeries():
# 	a,b = 0,1
# 	while b < 10:
# 		print(b)
# 		a,b = b,a+b

# FibonacciSeries()

# num=int(input('输入一个数字：'))
# if num%2 == 0:
# 	if num%3 == 0:
# 		print('可以整除2和3')
# 	else:
# 		print('只能整除2，不能整除3')
# else:
# 	if num%3 == 0:
# 		print('可以整除3，不能整除2')
# 	else:
# 		print('既不能整除3也不能整除2')

# import sys

# for arg in sys.argv[1:]:
# 	try:
# 		f = open(arg,'r')
# 	except IOError as e:
# 		print('cannot open',arg)
# 	else:
# 		print(arg,'has',len(f.readlines()),'lines')
# 		f.close()

# try:
# 	raise NameError('HiThere')
# except NameError as e:
# 	print('An exception flew by!')
# 	raise e

# if __name__ == '__main__':
# 	pass
# pass




# passline = 60
# def func(val):
# 	print('%x' % id(val)) # 查看变量名地址
# 	if val >= passline:
# 		print('pass')
# 	else:
# 		print('failed')
# 	def in_func(): # (val,)添加后是元组类型不能变的
# 		print(val) # 引用变量后说明变量添加到内函数属性中，使用时直接在内函数中查找
# 	in_func()
# 	return in_func
# # func(88)
# a =func(88)
# a()  #实际是调用了in_func()，相当于a和in_func指向同一个函数，a和in_func只是函数名
# print(a) #查看in_func()在func函数属性中的地址
# print(a.__closure__) # 查看in_func()中的属性是否存在val变量




# def my_sum(*arg):	
# 	return sum(arg)
# def my_average(*arg):
# 	return sum(arg)//len(arg)
# def dec(func):
# 	def in_dec(*arg):
# 		if len(arg) == 0: # 被除数不能为0
# 			return 0
# 		for val in arg: # 数据只能是int型
# 			if  not isinstance(val,int):
# 				return 0
# 		return func(*arg)
# 	return in_dec
# my_sum = dec(my_sum) # 1、先调用dec,2、再调用in_dec,3、再调用my_sum,4、再将my_sum函数名指向函数in_dec
# my_average = dec(my_average)

# print(my_sum(1,2,3,'2'))
# print(my_average())



# def dec(func):
# 	print('1、call dec')
# 	def in_dec(*arg):
# 		print('3、call in_dec')
# 		if len(arg) == 0:
# 			return 0
# 		for val in arg:
# 			if not isinstance(val,int):
# 				return 0
# 		return func(*arg)
# 	print('2、return in_dec')
# 	return in_dec
# print('装饰器代码执行顺序：')
# @dec # 等于my_sum = dec(my_sum)这句话
# def my_sum(*arg): # 装饰过后my_sum名指向in_dec函数对象，此时in_dec会调用原来的my_sum，要使用my_sum(1,2)才能调用
# 	print('4、call my_sum')
# 	return sum(arg)
# 	# print(sum(arg))
# def average(*arg):
# 	return sum(arg)//len(arg)

# print('调用被修饰的函数后才会执行闭包中的函数')
# print(my_sum(1,2,3))




# abs 求绝对值的函数
f = abs # 变量f指向函数
f(-20) # 直接调用函数


# 将abs指向另一个函数
abs = len
abs(-20)



























