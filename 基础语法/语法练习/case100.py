# coding=utf-8
# 2018-03-27
# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4.组成所有排列后再去掉不满足条件的排列

# count = 0 # 变量设为0的原因是最后输出的值不用再减一就可以直接拿出使用
# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if (i != k) and (i != j) and (j != k):
# 				print (i,j,k)
# 				# print(count) # 打印个数计算不能写在前面因为默认为0
# 				count +=1
# 				# print(count) # 个数计算
# print('总共 %d 个数'%(count))
# 扩展 ：
# for i in range(1,4):
# 	print(i)
# 	for j in range(1,4):
# 		print(' %d' % j)
# 		for k in range(1,4):
# 			print('   %d' % k)
# 			print(i,j,k)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目2：企业发放的奖金根据利润提成。利润（I）低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润（I），求应发奖金总数？
# 程序分析：请利用数轴来分界、定位。注意定义时需把奖金定义成长整型
# i = int(input('净利润：'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
# 	if i>arr[idx]:
# 		# print(r) # 查看自加前的值
# 		r += (i-arr[idx])*rat[idx]
# 		# print(r)  # 此时的r进行了叠加，不是某段利润的提成，而是某段提成的总和
# 		print(i - arr[idx])*rat[idx]
# 		i = arr[idx]
# print (r)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：
# 设该值为x
# 1、等式一：x + 100 = n^2, x + 100 + 168 = m^2
# 2、导出等式二：m^2 - n^2 = (m - n)(m + n) = 168
# 3、设置：m + n = i ,m - n = j, i * j = 168,i和j至少一个是偶数，因为个位数是8
# 4、可得出：m = (i + j)/2，n = (i - j)/2,i和j要么都是偶数，要么都是奇数,因为奇数+偶数除2不为整数
# 5、从3和4推导可知，i与j均是大于等于2的偶数
# 6、由于i * j =168, j>=2，则1<i<168/2+1
# 7、最后循环将i值循环计算
# 方法一：
# for i in range(1,85):
# 	if 168 % i == 0:
# 		j = 168 / i
# 		if i > j and (i+j) % 2 == 0 and (i - j) % 2 == 0:
# 			m = (i + j) / 2
# 			n = (i - j) / 2
# 			x = n **2 - 100
# 			print('m的值:%d，n的值:%d，i的值:%d，j的值:%d ' % (m,n,i,j))
# 			print('这个数是 %d ' % x)

# 方法二：使用math函数,但这个循环无法遍历到-99的情况，因为range(10000)是从0开始
# import math
# for i in range(10000):
# 	x = int(math.sqrt(i + 100))
# 	y = int(math.sqrt(i + 168 + 100))
# 	if(x*x == i + 100) and (y*y == i  + 168 + 100):
# 		print(i)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目4：输入某年某月某日，判断这一天是这一年的第几天
# 程序分析：以3月5日为例，应该先把前两个月的天数加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(raw_input('day:\n'))
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
# 	sum = months[month - 1]
# else:
# 	print('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
# 	leap = 1
# if (leap == 1) and (month > 2):
# 	sum += 1
# print('it is the %dth day.' % sum)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目5：输入三个整数x，y，z，请把这三个数由小到大输出
# 程序分析：把最小的数先放在x上，将x与y进行比较，如果x大则与y值进行交换，然后再用x与z进行比较，如果x大则与z值进行交换，这样x便最小
# 考察冒泡排序
# 方法一：使用冒泡排序
# l = []
# for i in range(3):
# 	x = int(input('输入一个整数：'))
# 	l.append(x)
# n = len(l)
# for j in range(n-1): # 该层循环控制 需要冒泡的轮数
# 	for i in range(n-1-j): # 该层循环用来控制每轮 冒出一个数 需要比较的次数
# 		if l[i]>l[i+1]:
# 			temp = l[i]
# 			l[i] = l[i+1]
# 			l[i+1] = temp
# l.sort()
# sort() 函数用于对原列表进行冒泡排序，如果指定参数，则使用比较函数指定的比较函数。
# print(l)

# 冒泡排序
# s = [92,21,11,7,4]
# n = len(s)
# for i in range(n-1):  # 该层循环控制 需要冒泡的轮数
# 	print(' 第%d轮' %i)
# 	# n-1的原因是列表下标j+1<n；-i的原因是i每循环一次就可以减少一次比较次数
# 	for j in range(n-1-i): # 该层循环用来控制每轮 冒出一个数 需要比较的次数
# 		print(j)
# 		if s[j]>s[j+1]:
# 			temp = s[j]
# 			s[j] = s[j+1]
# 			s[j+1] = temp
# 			print(s)
# print(s)

# 方法二：使用列表方法sort()
# l = []
# for i in range(3):
# 	x = int(input('请输入数据：\n'))
# 	l.append(x)
# l.sort()
# print(l)


#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 2018-3-28
# 题目6：斐波那契数列（Fibonacci sequence）
# 程序分析：又称黄金分割数列，指的是这样一个数列0、1、1、2、3、5...前两个数之和为第三个数
# 采用递归方法定义
# F0 = 0  (n=0)
# F1 = 1  (n=1)
# Fn = F[n-1] + F[n-2](n=>2)

# 方法一:
# def fib(n):
# 	a,b = 0,1
# 	for i in range(n-1): # 循环9次，但最后一次输出的是b
# 		a,b = b,a+b
# 	return b
# print (fib(10)) # 输出了第10个斐波那契数列

# 方法二：使用递归
# def fib(n):
# 	if n==1 or n==2:
# 		return 1
# 	elif n>1: # 做异常处理
# 		return fib(n-1)+fib(n-2)
# 	return '请输入大于0的整数'
# print(fib(0))

# 方法三：输出指定的序列n
# def fib(n):
# 	if n == 1:
# 		return[1]
# 	if n == 2:
# 		return[1,1]
# 	fibs = [1,1]
# 	for i in range(2,n):
# 		fibs.append(fibs[-1] + fibs[-2]) #下标-1表示倒数第一个数，-2表示倒数第二个数
# 	return fibs
# print (fib(0))
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目13：打印出所有“水仙花数”，所谓‘水仙花数’是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个‘水仙花数’，因153=1的三次方+5的三次方+3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位、十位、百位
# for n in range(100,1000):
# 	i = n // 100 # 百位取整,//代表相除取整
# 	j = n // 10 % 10 # 十位取整
# 	k = n % 10 # 个位取整
# 	if n == i**3 + j**3 + k**3:
# 		print(n)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
'''
题目：将一个正整数分解质因数。例如：输入90，打印出90=2*3*3*5
分析：对n进行分解质因数，应该先找到最小的质数k，然后按下述步骤完成：
1、如果这个质数恰好等于n，则说明分解质因数的过程已经结束，打印出即可
2、如果n<>i,但n能被i整除，则应打印出i的值，并用n除以i的商，作为新的正整数n，重复执行第一步
3、如果n不能被i整除，则用i+1作为i的值，重复执行第一步
'''
# from sys import stdout
# n = int(input('input number:\n'))
# print('n = %d' % n)

# for i in range(2,n+1): # i 为要求的质因数
# 	while n != 1:
# 		if n % i == 0:
# 			stdout.write(str(i))
# 			stdout.write('*')
# 			n = n / i
# 		else:
# 			break
# print('%d' % n)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
'''
题目18：求s=a+aa+aaa+aaaa+...+aaa...a的值，其中a是一个数字。
例如：2+22+222+2222+22222（此时共有5个数相加），几个数相加由键盘控制
分析：关键是计算出每一项的值
'''
# from functools import reduce
# Tn = 0
# Sn = []
# n = int(input('n = :\n'))
# a = int(input('a = :\n'))
# for count in range(n):
# 	Tn = Tn + a
# 	a = a * 10
# 	Sn.append(Tn)
# 	print (Tn)
# Sn = reduce(lambda x,y : x + y,Sn)
# print (Sn)
#reduce() 函数会对参数序列中元素进行累积,但已不在python3内置函数中。参考http://www.runoob.com/python/python-func-reduce.html

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
'''
题目19：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如：6=1+2+3.编程找出1000以内的所有完数
分析：对n进行分解质因数，应该先找到最小的质数k，然后按下述步骤完成：
1、如果这个质数恰好等于n，则说明分解质因数的过程已经结束，打印出即可
2、如果n<>i,但n能被i整除，则应打印出i的值，并用n除以i的商，作为新的正整数n，重复执行第一步
3、如果n不能被i整除，则用i+1作为i的值，重复执行第一步
'''
# from sys import stdout
# for j in range(2,1001): # j为要分解的数
# 	k = []
# 	n = -1 # 为了以列表的形式输出
# 	s = j # 用于做加法的变量计算
# 	for i in range(1,j): # i就是质因数
# 		if j % i == 0:
# 			n += 1
# 			s -= i 
# 			k.append(i)
# 	if s == 0:
# 		stdout.write('%d = '%j)
# 		for i in range(n): # 这个for语句主要是实现1+这种格式
# 			stdout.write(str(k[i]))
# 			stdout.write('+')
# 		print(k[n])

# 说明：列表双循环中，里面的循环是为了向列表中添加次数，外面的循环是增加轮数，每轮循环时列表k值都会被重置为初始值
# for j in range(2):
# 	k = []
# 	for i in range(1,3):
# 		print(k)
# 		k.append(i)
# 		k.append(i)
# 	print(k)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目：有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个序列的前20项之和
# 分析：对分子和分母设变量

# 方法一：使用临时变量t
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
# 	s += a / b
# 	t = a
# 	a = a + b
# 	b = t
# print(s)

# 方法二：使用python特有多变量赋值法
# a = 2.0
# b = 1.0
# s = 0.0
# for n in range(1,21):
# 	s += a / b
# 	b,a = a ,a + b
# print(s)

# 方法三：使用reduce函数
# from functools import reduce
# a = 2.0
# b = 1.0
# l = []
# for n in range(1,21):
# 	b,a = a,a+b
# 	l.append(a/b)
# print (reduce(lambda x,y:x + y,l))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目：利用递归算法求5！5的阶乘
# 分析：递归公式：fn = fn_1*4!
# def fact(j):
# 	sum = 0
# 	if j == 0:
# 		sum = 1
# 	else:
# 		sum = j * fact(j - 1) # 递归算法最先得出的是从最j=1开始
# 		print(sum)
# 	return sum 
# for i in range(6):
# 	print('%d! = %d' %(i,fact(i)))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 2018-03-29
# 题目7：将一个列表数据复制到另一个列表中
# 分析：使用列表[:]
# a = [1,2,3]
# b = a[:]
# print(b)


#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目8:输出9*9乘法口诀
# 分析：分行与列考虑，共9行9列，i控制行，j控制列

# for i in range(1,10):
# 	print(' ')
# 	for j in range(1,i+1):
# 		print('%d * %d=%d ' % (j,i,i*j),end=" ")

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目11：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月兔子总数为多少？
# 第一个月初有一对刚诞生的兔子，第二月仍然只有一对兔子，第二个月之后（第三个月初）它们可以生育，第三月就有2对兔子，第四月就有3对兔子（其中有1对是刚生的）
# 分析：规律为1，1，2，3，5，8，13....,斐波那契数列
# f1 = 1
# f2 = 1
# for i in range(1,22):
# 	print ('%12ld %12ld' % (f1,f2))
# 	if i%3 == 0:
# 		print('')
# 	f1 += f2
# 	f2 += f1
	
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目12：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
# 2018-4-7
# h = 0
# leap  = 1
# from math import sqrt
# from sys import stdout
# for m in range(101,201):
# 	k = int(sqrt(m+1))
# 	for i in range(2,k+1):
# 		if m % i == 0:
# 			leap = 0
# 			break
# 	if leap == 1:
# 		print('%-4d' % m)
# 		h += 1
# 		if h % 10 == 0: # 每10个数进行一次换行
# 			print('')
# 	leap = 1
# print('The total is %d ' % h)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目14：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
# from __future__ import print_function
# def reduceNum(n):	
#  	if not isinstance(n,int) or n <= 0:
#  		print('请输入一个正确的数字！')
#  		exit(0)
#  	elif n in [1]:
#  		print('1没有质因数')
#  	print('{} = '.format(n),end='') # end表示不换行
#  	# print('%d' % n) # 输出方式二
#  	while n not in [1]: # 循环保证递归
#  		for index in range(2,n+1):
#  			if n % index == 0:
#  				n //= index # ／／取整算法
#  				if n == 1:
#  					print(index)
#  				else: # index一定是素数
#  					print('{}*'.format(index),end='')
#  				break
# reduceNum(90)
# reduceNum(900)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目15：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

# score = int(input('输入分数：\n'))
# if score >= 90:
# 	grade = 'A'
# elif score >= 60:
# 	grade = 'B'
# else:
# 	grade = 'C'
# print('%d 属于 %s' % (score,grade))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目16：输出指定格式的日期。
# 程序分析：使用 datetime 模块。

# import datetime
# if __name__ == '__main__':

# 	# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
# 	print(datetime.date.today().strftime('%d/%m/%Y'))

# 	# 创建日期对象
# 	miyazakiBirthDate = datetime.date(1941,1,5)
# 	print(miyazakiBirthDate.strftime('%d/%m/%Y'))

# 	# 日期算术运算
# 	miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
# 	print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

# 	# 日期替换
# 	miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year+1)
# 	print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目17：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
# -------方法一：使用while循环---------
# import string
# s = raw_input('请输入一个字符串：\n')
# letters = 0
# space  = 0
# digit = 0
# others = 0
# i = 0
# while i<len(s):
# 	c = s[i]
# 	i +=1
# 	if c.isalpha():
# 		letters +=1
# 	elif c.isspace():
# 		space +=1
# 	elif c.isdigit():
# 		digit +=1
# 	else:
# 		others +=1
# print('char =%d,space = %d,digit =%d,others =%d' % (letters,space,digit,others))

#--------方法二：使用for循环-----------
# import string
# s = raw_input('请输入一个字符串：\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
# 	if c.isalpha(): # 判断是否是字母
# 		letters +=1
# 	elif c.isspace(): # 判断是否是空格
# 		space +=1
# 	elif c.isdigit(): # 判断是否是数字
# 		digit +=1
# 	else :
# 		others +=1
# print('char =%d,space =%d,digit =%d,others =%d' % (letters,space,digit,others))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目20：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# tour = []
# height = []
# hei = 100.0 # 起始高度
# tim = 10 # 次数
# for i in range(1,tim+1):
# 	if i == 1:
# 		tour.append(hei)
# 	else:
# 		tour.append(2*hei)
# 	hei /= 2
# 	height.append(hei)
# print('总高度：tour = {0}'.format(sum(tour)))
# print('第10次反弹高度：height = {0}'.format(height[-1]))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目21：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法，从后往前推断。
# x2 = 1
# for day in range(9,0,-1):
# 	x1 = (x2+1)*2
# 	x2 = x1
# 	print(day)
# print(x1)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目22：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
# for a in range(ord('x'),ord('z') + 1):
# 	for b in range(ord('x'),ord('z') + 1):
# 		if a != b:
# 			for c in range(ord('x'),ord('z')+1):
# 				if (a != c) and (b != c):
# 					if (a != ord('x')) and (c != ord('x')) and (c != ord('z')):
# 						print('order is a -- %s \t b -- %s \t c-- %s' % (chr(a),chr(b),chr(c)))
# print(ord('x'))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目23：打印出如下图案（菱形）
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

# from sys import stdout
# for i in range(4):
# 	for j in range(2-i+1):
# 		stdout.write(' ')
# 	for k in range(2*i+1):
# 		stdout.write('*')
# 	print()
# for i in range(3):
# 	for j in range(i+1):
# 		stdout.write(' ')
# 	for k in range(4-2*i+1):
# 		stdout.write('*')
# 	print()
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目24：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。 
# 方法一
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
# 	s += a/b
# 	t = a 
# 	a = a+b
# 	b = t
# print(s)
# 方法二：
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
# 	s += a/b
# 	b,a = a,a+b
# print(s)

#方法三：
# a = 2.0
# b = 1.0
# l = []
# l.append(a/b)
# for n in range(1,20):
# 	b,a = a,a+b
# 	l.append(a/b)
# print(reduce(lambda x,y: x+y,l)) # reduce在python中不是内置函数
# print(sum(l))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目25：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。 
# 方法一：
# n = 0
# s = 0
# t = 1
# for n in range(1,21):
# 	t *= n
# 	s += t
# print('1! + 2! + 3! +...+ 20! = %d' % s)

# 方法二
# s = 0
# l = range(1,21)
# def op(x):
# 	r = 1
# 	for i in range(1,x+1):
# 		r *= i
# 	return r
# s = sum(map(op,l))
# print('1! + 2! + 3! +...+ 20! = %d' % s)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目26：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4! 

# def fact(j):
# 	sum = 0
# 	if j == 0:
# 		sum = 1
# 	else:
# 		sum = j * fact(j-1)
# 	return sum
# print(fact(5))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目27：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def output(s,l):
# 	if l==0:
# 		return
# 	print(s[l-1])
# 	output(s,l-1)
# s = raw_input("Input a string: ")
# l = len(s)
# output(s,l)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目28：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

# def age(n):
# 	if n == 1:
# 		c = 10
# 	else:
# 		c = age(n-1) + 2
# 	return c
# print(age(5))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

# x = int(raw_input('请输入一个数：\n'))
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
# if a != 0:
# 	print('5位数：%d %d %d %d %d'% (e,d,c,b,a))
# elif b != 0:
# 	print('4位数：%d %d %d %d'% (e,d,c,b))
# elif c != 0:
# 	print('3位数：%d %d %d '% (e,d,c))
# elif d != 0:
# 	print('2位数：%d %d'% (e,d))
# else:
# 	print('1位数：%d'% e)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目30：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

# a = int(raw_input('请输入一个数字：\n'))
# x = str(a)
# flag = True

# for i in range(len(x)/2):
# 	if x[i] != x[-i - 1]:
# 		flag = Flase
# 		break
# if flag:
# 	print(' %d 是一个回文数！' % a)
# else:
# 	print(' %d 不是一个回文数！' % a)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目31：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

# letter = raw_input('please input:')
# if letter == 'S':
# 	print('please input second letter:')
# 	letter = raw_input('please input:')
# 	if letter == 'a':
# 		print('Saturday')
# 	elif letter == 'u':
# 		print('Sunday')
# 	else:
# 		print('data error')
# elif letter == 'F':
# 	print('Friday')
# elif letter == 'M':
# 	print('Monday')
# elif letter == 'T':
# 	print('please input second letter')
# 	letter = raw_input('please input:')

# 	if letter == 'u':
# 		print('Tuesday')
# 	elif letter == 'h':
# 		print('Thursday')
# 	else:
# 		print('data error')
# elif letter == 'W':
# 	print('Wednesday')
# else:
# 	print('data error')
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#

# 题目32：按相反的顺序输出列表的值。
# a = ['one','two','three']
# for i in a[::-1]:
# 	print(i)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目33：按逗号分隔列表。
# L = [1,2,3,4,5]
# s1 = '-'.join(str(n) for n in L)
# print(s1)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目34：练习函数调用。

# def hello_world():
# 	print('hello world')
# def three_hellos():
# 	for i in range(3):
# 		hello_world()
# if __name__ == '__main__':
# 	three_hellos()
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目35：文本颜色设置。运行后没有成功显示出颜色
# class bcolors:
# 	  HEADER = '\033[95m'
# 	  OKBLUE = '\033[94m'
# 	  OKGREEN = '\033[92m'
# 	  WARNING = '\033[93m'
# 	  FAIL = '\033[91m'
# 	  ENDC = '\033[0m'
# 	  BOLD = '\033[1m'
# 	  UNDERLINE = '\033[4m'
# print(bcolors.WARNING + '警告的颜色字体？' + bcolors.ENDC)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目36：求100之内的素数。
# # 输入指定范围的数据
# lower = int(input('输入区间最小值：'))
# upper = int(input('输入区间最大值：'))
# for num in range(lower,upper + 1):
# 	# 素数大于1
# 	if num > 1:
# 		for i in range(2,num): # for语句是否能够被整除
# 			if (num % i) == 0: 
# 				break
# 		else: # for语句的else,是素数直接打印出
# 			print(num)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目37：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

# if __name__ == '__main__':
# 	N = 10
# 	print('请输入10个数字：')
# 	l = []
# 	for i in range(N):
# 		l.append(int(raw_input()))
# 	print('你输入的数字是')
# 	for i in range(N):
# 		print(l[i])
# 	print
# # 排列10个数字
# 	for i in range(N - 1):
# 		min = i
# 		for j in range(i + 1,N):
# 			if l[min] > l[j]:
# 				min = j
# 		l[i],l[min] = l[min],l[i]
# 	print('排列之后：')
# 	for i in range(N):
# 		print(l[i])
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目38：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
# if __name__ == '__main__':
# 	a = []
# 	sum = 0
# 	for i in range(3):
# 		a.append([])
# 		for j in range(3):
# 			a[i].append(float(raw_input('input num:')))
# 	for i in range(3):
# 		sum += a[i][i]
# 	print(sum)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目39：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。 a
# a = [1,4,6,9,13,16,19,28,40,100,0]
# print('原始列表：')
# for i in range(len(a)):
# 	print('%d,'% a[i],end='')
# # number = int(raw_input('插入一个数字：'))
# number = 18
# end = a[9]
# if number > end:
# 	a[10] = number
# else:
# 	for i in range(10):
# 		if a[i] > number:
# 			temp1 = a[i]
# 			a[i] = number
# 			for j in range(i + 1,11):
# 				temp2 = a[j]
# 				a[j] = temp1
# 				temp1 = temp2 # 将插入后的元素向后摞一位
# 			break
# print('\n排序后列表')
# for i in range(11):
# 	print('%d,'% a[i],end='')
# print()

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目40：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。
# a = [9,6,5,4,1]
# N = int(len(a))
# print(a)
# for i in range(N//2):
# 	a[i],a[N-i-1] = a[N-i-1],a[i]
# print(a)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目41：模仿静态变量的用法。

# def varfunc():
# 	var = 0
# 	print('var = %d' % var)
# 	var += 1
# if __name__ == '__main__':
# 	for i in range(3):
# 		varfunc()
# class Static:
# 	StaticVar = 5
# 	def varfunc(self):
# 		self.StaticVar += 1
# 		print(self.StaticVar)
# print(Static.StaticVar)
# a = Static()
# for i in range(3):
# 	a.varfunc()
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目42：学习使用auto定义变量的用法。局部变量与全局变量的关系
# 程序分析：没有auto关键字，使用变量作用域来举例吧。
# num = 2 # 全局变量
# def autofunc():
# 	num = 1 # 局部变量
# 	print('internal block num = %d' % num)
# 	num += 1
# for i in range(3):
# 	print('The num = %d' % num)
# 	num += 1 # 全局变量
# 	autofunc()
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目43：模仿静态变量(static)另一案例。
# 程序分析：演示一个python作用域使用方法

# class Num:
# 	nNum = 1
# 	def inc(self):
# 		self.nNum += 1
# 		print('nNum = %d'%self.nNum)

# if __name__ == '__main__':
# 	nNum = 2
# 	inst = Num()
# 	for i in range(3):
# 		nNum += 1
# 		print('The num = %d'%nNum)
# 		inst.inc()
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
'''
题目44：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
'''
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
 
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# result = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(X)):
# 	for j in range(len(X[0])):
# 		result[i][j] = X[i][j] + Y[i][j]
# for r in result:
# 	print(r)
#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目45：统计 1 到 100 之和。
# tmp = 0
# for i in range(1,101):
# 	tmp += i
# print('The sum is %d '% tmp)

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目46：求输入数字的平方，如果平方运算后小于 50 则退出。
# TRUE = 1
# FALSE = 0
# def SQ(x):
# 	return x*x
# print('如果输入的数字小于 50，程序将停止运行')
# again = 1
# while again:
# 	num = int(raw_input('请输入一个数字：'))
# 	print('运算结果为 %d' % (SQ(num)))
# 	if SQ(num) >= 50:
# 		again = TRUE
# 	else:
# 		again = FALSE

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目47：两个变量值互换。
# def exchange(a,b):
# 	a,b = b,a
# 	return (a,b)
# if __name__ == '__main__':
# 	x = 10
# 	y = 20
# 	print('x = %d,y = %d' % (x,y))
# 	x,y = exchange(x,y)
# 	print('x = %d,y = %d' % (x,y))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目48：数字比较。
# i = 10
# j = 99
# if i > j:
# 	print('%d 大于 %d' % (i,j))
# elif i == j:
# 	print('%d 等于 %d' % (i,j))
# elif i < j:
# 	print('%d 小于 %d' % (i,j))
# else:
# 	print('未知')

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目49：使用lambda来创建匿名函数。 
# MAXIMUM = lambda x,y : (x > y) * x + (x < y) * y
# MINIMUM = lambda x,y : (x > y) * y + (x < y) * x
# a = 80
# b = 20
# print('The largar one is %d' % MAXIMUM(a,b))
# print('The lower one is %d' % MINIMUM(a,b))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#
# 题目50：输出一个随机数。
# 程序分析：使用 random 模块。

# import random
# print(random.uniform(10,20))

#～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～#





























