# 猫图财务后台结算页面
# 流程：0、生成结算订单，1、猫图财务选择结算公司，2、猫图财务发起车款结算，3、采销上传资料，4、合治审核车款结算，5、猫图财务发起落户报销，6、车务上传资料，7、合治审核报销结算
# 该页面有3个功能：选择结算公司、发起车款结算、发起落户报销

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

# 点击待结算订单
waitFinOrder = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[1]/div[1]/div[1]/div[1]/label[1]/span")
waitFinOrder.click()
time.sleep(3)


# 选择结算公司
selectFinCompang = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button/span")
selectFinCompang.click()
time.sleep(3)


compangList = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div")
compangList.click()
time.sleep(3)


sureButton = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div/div[2]/div[3]/button[1]/span")
sureButton.click()
time.sleep(8)
driver.close()







