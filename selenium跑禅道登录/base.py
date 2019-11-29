#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
#  重写了查找元素方法，加了显示等待。
# 重写了文本信息输入、点击事件、清除文本框数据事件等
# 与LoginPage.py关联
class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout=30
        self.poll=0.5

    def findElement(self,loctor):#loctor是元祖类型
        '''
        args:
        loctor 传元祖，如("id","xx")
        '''
        element = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElements(self,loctor):
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_elements(*loctor))
        return elements

    def sendKeys(self,loctor,text):
        ele=self.findElement(loctor)
        ele.send_keys(text)

    def click(self,loctor):
        ele=self.findElement(loctor)
        ele.click()

    def clear(self,loctor):
        ele=self.findElement(loctor)
        ele.clear()




if __name__=="__main__":
    driver = webdriver.Firefox()#实例化driver
    base=Base(driver)#实例化driver这个类

    driver.get("https://www.baidu.com")#打开百度
    loc1=("id","kw")#定位百度搜索框
    '''
    ele1=base.findElement(loc1)
    ele1.sendkeys("haode")
    '''
    base.sendKeys(loc1,"haode")


    loc2=("css selector","#su")#定位点击搜索按钮
    '''
    ele2=base.findElement(loc2)#*号后面的参数是一个list或者是一个元祖
    ele2.click()
    '''
    base.click(loc2)