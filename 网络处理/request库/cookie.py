# coding=utf-8
from selenium import webdriver
import time

class Cookie(object):
	"""docstring for Cookie"""
	def __init__(self, driver):
		super(Cookie, self).__init__()
		self.driver = driver
	def addCookie():
		self.driver.add_cookie()
		self.driver.add_cookie({'name':'PHPSESSID','value':'il986ta4b2r7tk4dubej12bn17'})
		self.driver.add_cookie({"name":"seller_id","value":"6334"})
		self.driver.add_cookie({'name':'user_type','value':'2'})
		self.driver.add_cookie({'name':'pro_name','value':'%E6%B5%AA%E7%90%B4%E6%9C%BA%E6%A2%B0%E6%89%8B%E8%A1%A8'})
		self.driver.add_cookie({'name':'pro_price','value':'12'})
		self.driver.add_cookie({'name':'gid','value':'38'})
		self.driver.add_cookie({'name':'bid','value':'862'})
		self.driver.add_cookie({'name':'month','value':'24'})
		self.driver.add_cookie({'name':'type','value':'1'})
		time.sleep(2)
# ----------------------------------------
s1 = requests.session()
r1 = s1.get("http://wap.test.fenqichaoren.com/Ms/Index/login.html")
# 登录前的cookie
print(r1.cookies)
print("----------------------")

# 添加登录后的cookie
c = requests.cookies.RequestsCookieJar()
c.set('PHPSESSID','091r5e4qsrj8n1u9pqbfdlv4r3')
c.set('seller_id','7535')
s1.cookies.update(c)

# 验证是否登录成功
centerUrl = "http://wap.test.fenqichaoren.com/Ms/Center/index.html"
writeMobile = "http://wap.test.fenqichaoren.com/Ms/Enter/writeMobile/t/sal.html"
commodityList = "http://wap.test.fenqichaoren.com/Ms/Enter/commodity.html"
# 身份证详情页面的必须cookie值需要知道，报错“用户类型参数或订单数据异常”，需要接口参数，此处阻塞
upload_idcard ="http://wap.test.fenqichaoren.com/Ms/Enter/upload_idcard/type/1/gid/53/bid/864"

r2 = s1.get(upload_idcard)
print(r2.text)
print(r2.cookies)







