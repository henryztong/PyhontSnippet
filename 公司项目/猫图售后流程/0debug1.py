from selenium import webdriver
import time
# 调试环境用
url = 'http://mtcsadmin.kq47.com/#/login'
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)