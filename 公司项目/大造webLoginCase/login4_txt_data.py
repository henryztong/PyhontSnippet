# coding=utf-8
from selenium import webdriver
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from userdata import *
from log_module import Loginfo
#从txt文本中获取登录信息
# d = webdriver.Firefox() # 打开浏览器
# d.get('https://cloud.ravvar.cn/#!/login/sign')
# time.sleep(2)
# d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[1]/a[3]').click()
# ele = d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input')
# ele.click()
# ele.send_keys('darseek1')
# time.sleep(2)
# d.close()


# 创建一个等待时间函数
def get_ele_times(driver,times,func):
	return WebDriverWait(driver,times).until(func)

def openBrower():
	webdriver_handle = webdriver.Firefox()
	return webdriver_handle

def openUrl(d,url):
	d.get(url)
	# d.maximize_window() # 最大化窗口

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
		eletuple[i].send_keys(' ') # 确认文本框位置
		eletuple[i].clear()  # 清空文本框
		eletuple[i].send_keys(arg[key]) # 输入用户名密码
		i+=1
	# 加一个异常处理登录按钮元素设有一个<div id="tooltip">作为蒙层,需要时间让其消失)
	try:
		eletuple[2].click() # eletuple[2]返回的值是login_ele
		print("点击1次登录")
	except Exception as e:		
		try:
			print("重新尝试点击")
			eletuple[0].click() 
			time.sleep(1)
			eletuple[2].click()
			print("成功点击登录按钮")
		except Exception as e:
			print("登录失败，5秒后关闭")
	
def checkResult(d,error1,error2,error3,errclick,arg,log):
	# 这里的try是解决找不到元素抛出异常的问题。也可以写在每个if语句中
	result = False # 设置一个变量默认为Flase，当登录成功则变为true
	print('start')
	try:	
		if d.find_element_by_xpath(error1).text :
			err1 = d.find_element_by_xpath(error1).text # 获取元素的文本信息
			print(err1)  #python2.7的编码格式是ASCII，输出需要转码
			errmsg = '用户名：%s,密码：%s;错误信息:%s\n'%(arg['uname'],arg['pwd'],err1)#公司环境
			log.log_write(errmsg)
		elif d.find_element_by_xpath(error2).text :
			err2 = d.find_element_by_xpath(error2).text
			print(err2) 
			errmsg = '用户名：%s,密码：%s;错误信息:%s\n'%(arg['uname'],arg['pwd'],err2)
			log.log_write(errmsg)
		else:		
			err3 = d.find_element_by_xpath(error3).text
			print(err3) 
			errmsg = '用户名：%s,密码：%s;错误信息:%s\n'%(arg['uname'],arg['pwd'],err3) # 将信息进行拼接#公司环境
			log.log_write(errmsg)#公司环境	
			d.find_element_by_xpath(errclick).click()
	except:
		msg = '用户名：%s,密码：%s;登录成功\n'%(arg['uname'],arg['pwd'])  # 将信息进行拼接
		log.log_write(msg)
		print("登录成功，Right!")
		result = True	
	print(result)
	time.sleep(3)
	return result
	
def logout(d,ele_dict):
	d.find_element_by_xpath(ele_dict['usermenu']).click()
	print("退出成功，等待下次登录")
	# time.sleep(3)
	d.find_element_by_xpath(ele_dict['logout']).click()
	time.sleep(3)

def login_test(dict,user):
	d = openBrower() # 打开浏览器
	openUrl(d,dict['url']) # 打开地址
	log = Loginfo() # 创建一个log实例对象,用来存放日志信息
	ele_tuple = findElement(d,dict)  # 查找元素位置，将返回的元组赋给一个变量
	for arg in user:
		sendVals(d,ele_tuple,arg) 
		result = checkResult(d,dict['errorid1'],dict['errorid2'],dict['errorid3'],dict['layer-btn'],arg,log) # 检查异常情况
		if result:		# 登录成功的账号需要先注销后再进行登录
			# logout,注销方法
			logout(d,dict)
			# login，重新查找元素位置
			ele_tuple = findElement(d,dict)  # 将返回的元组赋给一个变量
	print('end')
	log.log_close()
	time.sleep(3)
	d.close()


if __name__ == '__main__':
	'''
	ele_dict = {'url':url,'user_xpath':login_text,'account_xpath':'/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input',
				'pwd_xpath':'/html/body/div[1]/div[2]/div/div/div/div/form/div[3]/input','login_xpath':'login-btn',
				'errorid':'用户名不能为空!'}
	user_list = [{'uname':account,'pwd':pwd}] # 列表中可以存放多个字典，也就是说可以存放多个用户名和密码
	'''
	# 将数据存放在txt文件中，从txt文件获取数据
	user_list = get_userinfo(r'G:\case\userinfo.txt')  #公司环境
	ele_dict = get_webinfo(r'G:\case\webinfo.txt')

	# user_list = get_userinfo(r'D:\Learn\case\userinfo.txt') 
	# ele_dict = get_webinfo(r'D:\Learn\case\webinfo.txt')
	login_test(ele_dict,user_list)



