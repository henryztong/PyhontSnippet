#登录页面
from selenium import webdriver
import time
# 调试环境用
# url = 'http://mtcsadmin.kq47.com/#/login'
# # driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)


class Login(object):
	"""登录类封装"""
	def __init__(self, driver):
		super(Login, self).__init__()
		self.driver = driver

	def input_user(self,driver):
		# 封装输入用户的方法
		account_ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[1]/div/div[1]/input')
		account_ele.clear()
		account_ele.send_keys('hzjs')

	def input_psw(self,driver):
		# 封装输入密码的方法
		pwd_ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[2]/div/div[1]/input')
		pwd_ele.clear()
		pwd_ele.send_keys('123456')

	def select_keep_login(self):
		# 下次自动登录,该网页无该功能
		pass

	def click_login(self,driver):
		# 点击登录按钮方法
		login_ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/button')
		login_ele.click()

if __name__ == '__main__':
	# begin = Login(driver)
	# begin.input_user(driver)
	# begin.input_psw(driver)
	# begin.click_login(driver)
	# time.sleep(5)
	# driver.close()
	pass