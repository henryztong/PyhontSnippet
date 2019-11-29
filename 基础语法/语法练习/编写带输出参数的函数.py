# 1. 通过返回一个结果元组：
def function1(a,b):
	a = 'new-value'
	b = b+1
	return a,b

x,y = 'old-value',99
x,y = function1(x,y)
print(x,y)

# 2. 通过传递可变对象，列表
def function2(a):
	a[0] = 'new-value'
	a[1] = a[1]+1
a = ['old-value',99]
function2(a)
print(a[0],a[1])

# 3. 通过传递可变对象，字典
def function3(args):
	args['a'] = 'new-value'
	args['b'] = args['b'] +1
args={'a':'old-value','b':99}
function3(args)
print(args['a'],args['b'])


# 4. 在一个实例中捆绑值：
class callByRef(object):
	"""docstring for callByRef"""
	def __init__(self,**args):
		for key,value in args.items():
			# setattr方法的作用原文：https://www.cnblogs.com/caicairui/p/7859490.html
			setattr(self,key,value)
def function5(args):
	args.a = 'new-value'
	args.b = args.b+1	
args=callByRef(a='old-value',b=99)
function5(args)
print(args.a,args.b)











