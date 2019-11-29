# requests安装 pip install requests
import requests
res = requests.get("http://www.baidu.com")
res = requests.post("http://www.baidu.com")
a = "15528101303"
params = {
	'name': 'henry',
	'password': '123456',
	'iphone':'%s'%a
}

# res = requests.get(url,params,headers)
# res = requests.post(url,data,json,headers)

# 查看响应信息
print(res.text) # 文本信息
print(res.status_code) # 响应http状态码
print(res.url)
print(res.content) # 二进制流信息，会自动解码gzip和deflate压缩
print(res.encoding) # 编码格式
print(res.cookies)
print(res.headers) # 响应头，字典的键不区分大小写，若键不存在则返回None
print(res.json) # requests中内置json解码器
print(res.raw) # 返回原始响应体
print(res.raise_for_status()) # 失败请求抛出异常
# -----------------------------------------------------

# 在字典中使用变量的两种方法
a = 'henry'
b = '123456'
par = {
	'name':a, # 方法1
	'password':'%s'%b, #方法2
}
print(par)
# -----------------------------------------------------
# 解决SSL证书校验,verify默认为True，在https请求时应关闭掉
requests.get('http:github.com',verify=False)


# 禁用安全警告
import urllib3
urllib3.disable_warnings()

# -----------------------------------------------------
# post上传的body的4种格式
# 1、application/json，常用
# 2、application/x-www-form-urlencoded，常用
# 3、multipart/form-data:表单格式
# 4、text/xml

当Body为json时，表示自动将python里面的字典转化为json格式参数。
当Body为data时，以字典的形式传递，如果其中包含json，则将其值改为str。

headers里面的重要属性有cookie,contentType,user-agent,X-Requested-With

# 查看请求头中的content-type属性来判断参数类型是json或data，都以字典的形式展示

# body中的数据格式：data和json选其一，不要两个都传

# 如何区分data和json数据：
1、通过content_type类型查看，值是application/json为json，值是application/x-www-form-urlencoded为data
2、看数据的表现形式，一般json格式：{'name':'value1','name2':'value2'};data格式：name=value1&name2=value2


注意：请求的地址可能遇到302重定向









































