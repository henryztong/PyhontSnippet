# 采销获取待结算订单列表接口
# 流程：0、生成结算订单，1、猫图财务选择结算公司，2、猫图财务发起车款结算，3、采销上传资料，4、合治审核车款结算，5、猫图财务发起落户报销，6、车务上传资料，7、合治审核报销结算
import requests
import ast
import json
from LoginApp import loginToken
url = "http://mtcsapi.kq47.com/v1/op/finances"
tokenTemp = loginToken() # 创建一个实例对象,以便获取用户token
# print(token1.getToken())

querystring = {"page":"1","size":"10","status":"5"}
headers = {
    'page': "1",
    'token': tokenTemp.getToken(), # 调用getToken方法
    'status': "35",
    }
# 获取结算订单列表
response = requests.request("GET", url, headers=headers, params=querystring)
# 将响应体转化为字典类型
response_dict2 = json.loads(response.text)

# print(type(response_dict2['models'])) # 查看响应类型
# print(response_dict2['models'][0]['id']) # 取出financialID
# print(type(response_dict2['models'][0]['id'])) # 查看ID类型

financesId = str(response_dict2['models'][0]['id']) #获取结算订单ID
url = "http://mtcsapi.kq47.com/v1/op/finances/"+financesId+"/car/service/supply"


# 提交车务数据，车务填数据：purchase_tax购置税、vav_tax车船税、strong_insurance交强险、commercial_insurance商业险
payload = "{\r\n    \"images\":\r\n    {\r\n        \"0\": \"http://p82xaw1nf.bkt.clouddn.com/222.png\",\r\n        \"1\": \"http://p82xaw1nf.bkt.clouddn.com/222.png\",\r\n        \"2\": \"http://p82xaw1nf.bkt.clouddn.com/222.png\"\r\n    },\r\n    \"purchase_tax\":5400,\r\n    \"vav_tax\": 390 ,\r\n    \"strong_insurance\": 1000,\r\n    \"commercial_insurance\":4390\r\n}"
headers = {
    'Content-Type': "application/json",
    'token': tokenTemp.getToken(),
    # 'Cache-Control': "no-cache",
    # 'Postman-Token': "e26388bc-7232-4513-aaa7-fabfd2ef3242"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)




