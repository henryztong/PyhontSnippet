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
# //*[@id="sign"]/div/div/div/form/div[1]/a[3]
account = 'darseek1'
pwd = '123456'

# 创建一个等待时间函数
def get_ele_times(driver,times,func):
	return WebDriverWait(driver,times).until(func)

def login_test():
	d = webdriver.Firefox() # 打开浏览器
	# d = webdriver.Safari()
	d.get(url)

	d.maximize_window() # 最大化窗口
	ele_login = get_ele_times(d,5,\
		lambda d: d.find_element_by_xpath(login_text)) # 找到用户名登录
	ele_login.click()

	account_ele = d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input')
	account_ele.send_keys(' ')
	account_ele.clear()
	account_ele.send_keys(account)

	pwd_ele = d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[3]/input')
	pwd_ele.send_keys(' ')
	pwd_ele.clear()
	pwd_ele.send_keys(pwd)
	time.sleep(5)  # 按钮元素设有一个<div id="tooltip">作为蒙层
	d.find_element_by_class_name('login-btn').click()
	# d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div[5]/button').click()
	time.sleep(12)
	d.close()
if __name__ == '__main__':
	login_test()












