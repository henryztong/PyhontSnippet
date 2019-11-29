# 如何实现switch语句



def switch_demo(value):
	switcher = {
	0:'zero',
	1:'one',
	2:'two'
	}
	return switcher.get(value,'没有匹配到值')

if __name__ == '__main__':
	a = switch_demo(4)
	print(a)