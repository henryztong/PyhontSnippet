# 后台admin管理后台
# 流程：0、生成结算订单，1、猫图财务选择结算公司，2、猫图财务发起车款结算，3、采销上传资料，4、合治审核车款结算，5、猫图财务发起落户报销，6、车务上传资料，7、合治审核报销结算
# 该页面功能：生成结算订单，分派给猫图财务
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

# 进入订单列表
menu_order = driver.find_element_by_link_text("订单")
menu_order.click()
time.sleep(3) # 等待列表加载

# 指派猫图财务:1、点击图标
caiwu_icon = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/i")
# caiwu_icon.click()
actions = ActionChains(driver)
actions.move_to_element(caiwu_icon) #将鼠标移动到y要点击的元素
actions.click(caiwu_icon)
actions.perform()
time.sleep(3)

# 指派猫图财务:2、选择猫图财务
# caiwu_list = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div")
caiwu_list = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr")
caiwu_list.click()


# 指派猫图财务:3、点击确定
sure_button = driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div/div[2]/div[3]/button[1]/span")
sure_button.click()
time.sleep(8)
driver.close()












