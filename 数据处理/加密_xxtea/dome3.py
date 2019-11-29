import xxtea,base64,json
import urllib.parse
from hashlib import sha1
from hebao_import import input_data
"""		
和包加密步骤
接口的所有参数  => 排序json  => URLEncoder json_str   =>sha1 得到 messageSignStr  =>  jsonStr + messageSignStr xxtea =>得到 jsonValue  
请求参数  reqData=jsonValue +  clientId  => json 请求
-------------
和包解密步骤
获取到 clientId 和  reqData
reqData  xxtea=>解密 =>  字符串分隔 =>  jsonStr + messageSignStr  =>验签(jsonStr排序,URLEncoder,sha1) 得到sign  =>  sign 对比  messageSignStr
"""

# 读取文本中的值作为参数
path = './hebao_param.txt'
data = input_data()
pythonStr = data.get_data(path)
print('字段 %s'%pythonStr)

# 排序
list_key = sorted(pythonStr)
# print(list_key)

list_value =[]
for x in list_key:
	list_value.append(pythonStr[x])
	# print(pythonStr[x])
# print(list_value)

sortStr = dict(zip(list_key,list_value)) 
print('排序 %s'%sortStr)


# 转json
jsonStr = json.dumps(sortStr)
print('转json %s'%jsonStr)


# URLEncoder编码
codes = urllib.parse.quote(jsonStr,'utf-8')
print('URLEncoder编码 %s'%codes)


# sha1加密
s1 = sha1()
s1.update(codes.encode())
messageSignStr = s1.hexdigest() # 16位密码，40位字符串
print('sha1加密 %s'%messageSignStr)

# 字符串拼接
messageSignStr = jsonStr + messageSignStr
print('字符串拼接 %s'%messageSignStr)

# xxtea加密
key = "jT1kdbpWtdxQDDr9uC7/E5Hi4RaoFYg1"
jsonValue = xxtea.encrypt(messageSignStr, key)
jsonValue = base64.b64encode(jsonValue)
jsonValue = bytes.decode(jsonValue)
print('xxtea加密 %s'%jsonValue)
print(type(jsonValue))
