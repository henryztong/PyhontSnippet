# 移动端登录接口

import requests
import ast
# 测试地址
url = "http://mtcsapi.kq47.com/v1/op/login"
# 请求体中填写用户名、密码，密码是md5的方式加密过的
payload = "{\n  \"username\":\"chewu\",\n  \"password\":\"e10adc3949ba59abbe56e057f20f883e\"\n}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
   # 'Postman-Token': "f814e5d9-b7e5-4fca-a6b1-b9fd393874a8"
    }
# 发送请求
response = requests.request("POST", url, data=payload, headers=headers)
response_dict = ast.literal_eval(response.text) # 将响应体转化为字典类型
# print(response.text)
# print(response_dict['token'])


class loginToken(object):
	"""docstring for loginToken"""
	def __init__(self):
		super(loginToken, self).__init__()
			
	def getToken(self):
		# print(response_dict['token'])
		return response_dict['token']

