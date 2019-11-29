import json
import requests
import urllib
d1 = {
	'a':None,
	'b':False,
	'c':True,
	'd':'bab2',
	'e':['1',22],
	'f':('ln',88),
	"g":{
	'h':1,
	'i':'12',
	'j':True,
	'k':'你好'
	}

}

# print(type(d1))
# js = json.dumps(d1)
# print(type(js))
# print(js)
# py = json.loads(js)
# print(type(py))
# print(py)


# payload = {
# 	"yoyo":"hello world!",
# 	"python":12345,
# 	"requests":True
# }
# url = "http://www.baidu.com"
# r1 = requests.post(url,json=payload) # 通过json参数直接将payload字典转json格式
# # print(r1.text)
# print(r1.content) 

# aa = "{\"1\":false}"
# print(type(aa))
# r1 = json.loads(aa)
# print(type(r1))
# print(r1)


# a = '你好'
# # print(help(urllib))
# b = urllib.parse.quote(a)
# url = 'http://www.baidu.com?%s'%b
# print(url)


# r = requests.get('http://www.baidu.com?%s'%a)
# print(r.url)

a = 'hello'  '000 '
b = '123,%s'
c = ('888')

print(b % (c))
print(type(c))

