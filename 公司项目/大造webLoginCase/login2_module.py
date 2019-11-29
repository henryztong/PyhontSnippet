# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
# d = webdriver.Firefox() # 打开浏览器
# d.get('https://cloud.ravvar.cn/#!/login/sign')
# time.sleep(2)
# d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[1]/a[3]').click()
# ele = d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input')
# ele.click()
# ele.send_keys('darseek1')
# time.sleep(2)
# d.close()


url = 'https://cloud.ravvar.cn/#!/login/sign'
login_text = '/html/body/div[1]/div[2]/div/div/div/div/form/div[1]/a[3]'
account = 'darseek1'
pwd = '123456'

# 创建一个等待时间函数
def get_ele_times(driver,times,func):
	return WebDriverWait(driver,times).until(func)

def openBrower():
	webdriver_handle = webdriver.Firefox()
	return webdriver_handle

def openUrl(d,url):
	d.get(url)
	d.maximize_window() # 最大化窗口

def findElement(d,arg):
	'''
	1: user_xpath
	2: account_xpath
	3: pwd_xpath
	4: login_xpath
	return useEle,pwdEle,loginEle
	'''
	if 'user_xpath' in arg: # 判断标签是否存在
		ele_user = get_ele_times(d,5,\
		lambda d: d.find_element_by_xpath(arg['user_xpath'])) # 找到用户名标签
		ele_user.click()

	account_ele = d.find_element_by_xpath(arg['account_xpath']) # 找到用户文本框
	pwd_ele = d.find_element_by_xpath(arg['pwd_xpath']) # 找到密码文本框
	login_ele = d.find_element_by_class_name(arg['login_xpath']) # 找到登录按钮
	return account_ele,pwd_ele,login_ele # 返回的是元组

def sendVals(d,eletuple,arg):
	'''
	参数包括
	ele tuple 一个包含元素数据的元组
	account:uname,pwd  一个包含用户名密码的字典
	'''
	listkey = ['uname','pwd']
	i = 0 
	for key in listkey: # 循环2次，第1次当i=0时元组中eletuple[0]为account_ele，第2次当i=1时元组中eletuple[1]pwd_ele
		eletuple[i].send_keys(' ')
		eletuple[i].click()
		eletuple[i].send_keys(arg[key])
		i+=1
	
	# 登录按钮元素设有一个<div id="tooltip">作为蒙层,需要时间让其消失)
	try:
		# time.sleep(2) 
		eletuple[2].click() # eletuple[2]返回的值是login_ele
		print("点击1次登录")
		# time.sleep(2) 
	except Exception as e:
		try:
			print("重新尝试点击")
			eletuple[0].click() 
			time.sleep(1)
			eletuple[2].click()
			print("成功点击登录按钮")
		except Exception as e:
			print("登录失败，5秒后关闭")
	
	
def checkResult(d,text):
	try:
		d.find_element_by_link_text(text)
		print("Error!")
	except:
		print("登录成功，Right!")

def login_test():
	d = openBrower() # 打开浏览器
	openUrl(d,url) # 打开地址

	# 元素的webdriver数据
	ele_dict = {'user_xpath':login_text,'account_xpath':'/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input',
				'pwd_xpath':'/html/body/div[1]/div[2]/div/div/div/div/form/div[3]/input','login_xpath':'login-btn'}
	# 登录用户名和密码数据
	account_dict = {'uname':account,'pwd':pwd}


	ele_tuple = findElement(d,ele_dict)  # 将返回的元组赋给一个变量
	sendVals(d,ele_tuple,account_dict) 
	
	checkResult(d,'用户名不能为空!') #
	time.sleep(2)
	d.close()


if __name__ == '__main__':
	login_test()



