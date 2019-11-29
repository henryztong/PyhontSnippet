# 原文：https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions
# 默认值是在 定义过程 中在函数定义处计算的


# 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数：
def f(a,L=[]):
	print(L)
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))


# 如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:
def f(a,L=None):
		print(L)
		if L is None:
			L=[]		
		L.append(a)
		return L
print(f(1))
print(f(2))
print(f(3))
print(f(3,L=[]))







