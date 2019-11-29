https://blog.csdn.net/weixin_41829272/article/details/80658586

列表生成式 : 中括号括起来表示列表
(1)[exp for iter_var in iterable if_exp] 
#工作过程： 
1 迭代iterable中的每个元素，每次迭代都先判断if_exp表达式结果为真，如果为真则进行下一步，如果为假则进行下一次迭代； 
2 把迭代结果赋值给iter_var，然后通过exp得到一个新的计算值； 
3 最后把所有通过exp得到的计算值以一个新列表的形式返回。 

#相当于这样的过程： 
L = [] 
for iter_var in iterable: 
	if_exp: 
		L.append(exp) 

#也可以循环嵌套 
(2)[exp for iter_var_A in iterable_A for iter_var_B in iterable_B] 工作过程： 每迭代iterable_A中的一个元素，就把ierable_B中的所有元素都迭代一遍。 

#相当于这样的过程： L = [] for iter_var_A in iterable_A: for iter_var_B in iterable_B: L.append(exp)
---
字典推导式:大括号括起来,表示为字典
d = {key: value for (key, value) in iterable} 
#快速更改字典key,value 
mcase = {'a': 10, 'b': 34} 
mcase_frequency = {v: k for k, v in mcase.items()} 
print(mcase_frequency) #  Output: {10: 'a', 34: 'b'}
