#原文： https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions
# lambda a, b: a+b
# 表达式
# https://docs.python.org/zh-cn/3/reference/expressions.html#lambda


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# key=lambda pair: pair[1]


# print(key)
# print(str(key))


pairs.sort(key=lambda pair: pair[1])
print(pairs)



def make_incrementor(n):
	print(n)
	# print(x)
	return lambda x: x + n
f = make_incrementor(42)

# print(f(0))
print(f(2))
















