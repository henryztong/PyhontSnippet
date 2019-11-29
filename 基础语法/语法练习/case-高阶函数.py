# coding=utf-8
'''
https://www.imooc.com/code/6047
python把函数作为参数
例子：
利用add(x,y,f)函数，求x的开方，y的开方
'''
import math
def add(x,y,f):
	return f(x) + f(y)
print(add(25,9,math.sqrt))


#—————————————————————————————————————————————————————#
'''
4-map()函数
https://www.imooc.com/code/6049
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
'''
# 例子：求列表中每个元素的平方
def f(x):
	return x*x
l = list(map(f,[1,2,3,4]))
print(l)


# 例子：假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
# 输入：['adam', 'LISA', 'barT']
# 输出：['Adam', 'Lisa', 'Bart']

# 分析：format_name(s)函数接收一个字符串，并且要返回格式化后的字符串，利用map()函数，就可以输出新的list。
def format_name(s):
	return s[0].upper() + s[1:].lower()
l = list(map(format_name,['admin','LISA','barT']))
print(l)

#—————————————————————————————————————————————————————#
'''
5-reduce()函数
https://www.imooc.com/code/6050
reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
reduce()还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100
reduce在python3中不再是默认函数，需要倒入functools
'''

# 题目：Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
# 输入：[2, 4, 5, 7, 12]
# 输出：2*4*5*7*12的结果
# 分析：reduce()接收的函数f需要两个参数，并返回一个结果，以便继续进行下一轮计算。
from functools import reduce
def prod(x,y):
	return x*y
print(reduce(prod,[2,4,5,6,7]))

#—————————————————————————————————————————————————————#
'''
6-filter()函数
https://www.imooc.com/code/6051
ilter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
'''
# 例子：利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
def is_not_empty(s):
	return s and len(s.strip())>0
l = list(filter(is_not_empty,['test',None,'','str','   ','End']))
print(l)

# 函数：s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：
a = ' 123\t\n'
l = a.strip()
print(l)


# 题目：请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 分析：filter() 接收的函数必须判断出一个数的平方根是否是整数，而 math.sqrt()返回结果是浮点数。
import math
def is_sqr(x):
	r = int(math.sqrt(x))
	return r*r == x
l = list(filter(is_sqr,range(1,101)))
print(l)

#—————————————————————————————————————————————————————#
'''
7-自定义排序函数
https://www.imooc.com/code/6053
sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
该方法穿2个参数比较只能在python2中使用
'''

# 实现倒序排序，只需要编写一个reversed_cmp函数：
# from functools import sorted
# def reversed_cmp(x,y):
# 	if x>y:
# 		return -1
# 	if x<y:
# 		return 1
# 	return 0

# l = sorted([36,44,54,4,6,35],reversed_cmp)
# print(l)

#—————————————————————————————————————————————————————#
'''
 8-返回函数
https://www.imooc.com/code/6054
Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
'''
# 题目：请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
# 分析：先定义能计算乘积的函数，再将此函数返回。
from functools import reduce
def calc_prod(lst):
	def lazy_prod():
		def f(x,y):
			return x*y
		return reduce(f,lst,1)
	return lazy_prod
f = calc_prod([1,2,3,4])
print(f())

#—————————————————————————————————————————————————————#
'''
9-闭包
https://www.imooc.com/code/6059
像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。

题目：返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
分析：
考察下面的函数 f:

def f(j):
    def g():
        return j*j
    return g

它可以正确地返回一个闭包g，g所引用的变量j不是循环变量，因此将正常执行。

在count函数的循环内部，如果借助f函数，就可以避免引用循环变量i。
'''
def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		r = f(i)
		fs.append(r)
	return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

#—————————————————————————————————————————————————————#
'''
12-编写无参数decorator
https://www.imooc.com/code/6065
Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。
'''
# 题目：请编写一个@performance，它可以打印出函数调用的时间。
# 分析：计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。

import time
def performance(f):
	def fn(*args,**kw):
		t1 = time.time()
		r = f(*args,**kw)
		t2 = time.time()
		print('call %s() in %fs' % (f.__name__,(t2-t1)))
		return r
	return fn
@performance
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))

#—————————————————————————————————————————————————————#
'''
如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数，类似这样：
@log('DEBUG')
def my_func():
    pass
'''
# 题目：上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：
# 分析：要实现带参数的@performance，就需要实现：my_func = performance('ms')(my_func)，需要3层嵌套的decorator来实现。

import time
def performance(unit):
	def perf_decorator(f):
		def wrapper(*args,**kw):
			t1 = time.time()
			r = f(*args,**kw)
			t2 = time.time()
			t = (t2 - t1)*1000 if unit == 'ms' else (t2-t1)
			print('call %s() in %f %s' % (f.__name__,t,unit))
			return r
		return wrapper
	return perf_decorator
@performance('ms')
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))
#—————————————————————————————————————————————————————#
'''
调用@functools.wraps(f)来将原函数的属性传给新函数
由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。这对于那些依赖函数名的代码就会失效。
'''

import functools
def log(f):
	@functools.wraps(f)
	def wrapper(*args,**kw):
		print('call...')
		return f(*args,**kw)
	return wrapper
@log
def f2(x):
	pass
print(f2.__name__)

# 注意@functools.wraps应该作用在返回的新函数上。
import time,functools
def performance(unit):
	def perf_decorator(f):
		@functools.wraps(f)
		def wrapper(*args,**kw):
			t1 = time.time()
			r = f(*args,**kw)
			t2 = time.time()
			t = (t2-t1)*1000 if unit == 'ms' else (t2-t1)
			print('call %s() in %f %s' % (f.__name__,t,unit))
			return r
		return wrapper
	return perf_decorator
@performance('ms')
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial.__name__)

#—————————————————————————————————————————————————————#
'''
15-偏函数
https://www.imooc.com/code/6068
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
所以，functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
'''
# import functools
# sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2: cmp(s1.upper(),s2.upper()))
# print(sorted_ignore_case(['bob','about','Zoo','Credit']))













