import re


a = "联系人: 张三, 联系人: 李四"

b = "a联系人: 张雷 先生（合约部） 电话: 86 13881875952 1"

match_name = re.match('联系人*李四',a)
search_name = re.search('联系人*',a)

print(match_name)
print(search_name)


pattern = re.compile(r'\d+') 
m = pattern.match('one12twothree34four',3) 
# print(m)


pattern1 = re.compile('(联系人: [\u4e00-\u9fa5]*)|(电话: [0-9]* [0-9]* [0-9]*)')

# k = pattern1.findall(b)
k = pattern1.finditer(b)

print(k)

for x in k:
  print(x.group())



pattern1 = re.compile('联系人')
j = pattern1.split(b)

print(j)


