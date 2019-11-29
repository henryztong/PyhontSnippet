# 合治结算页面：确认结算操作
# 流程：0、生成结算订单，1、猫图财务选择结算公司，2、猫图财务发起车款结算，3、采销上传资料，4、合治审核车款结算，5、猫图财务发起落户报销，6、车务上传资料，7、合治审核报销结算
# 该页面有2个功能：审核车款结算、审核报销结算
from selenium import webdriver
from LoginAdminWeb import Login
from selenium.webdriver import ActionChains
import time
url = 'http://mtcsadmin.kq47.com/#/login'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

# 登录
login = Login(driver)
login.input_user(driver)
login.input_psw(driver)
login.click_login(driver)
time.sleep(3) # 等待页面加载

# 点击结算
FinButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div/ul/li[13]/a")
FinButton.click()
time.sleep(3)

# 点击确认已付款
surePay = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[1]/div[2]/div[3]/table/tbody/tr/td[9]/div/button/span")
surePay.click()

# 查看详情
# detail = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[1]/div[2]/div[3]/table/tbody/tr/td[3]/div")
# detail.click()

time.sleep(5)
driver.close()