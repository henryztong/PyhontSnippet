from selenium import webdriver
import unittest
from loginpage import LoginPage
from editbug import NewBug

# 测试用例的执行，用例为添加一个bug，没有使用unittest框架
        driver=webdriver.Firefox()
        loginpage=LoginPage(driver)
        newbug=NewBug(driver)

        loginpage.login()
        # 2.点【测试】，【bug】，【提交bug】
        newbug.click_test_tab()
        newbug.click_bug()
        newbug.click_add_bug()
        # 3.编辑bug
        newbug.add_truk()
        newbug.input_bug_title(bugtitle)

        driver.switch_to.frame(0)
        sendKeys(self.body_loc, text)
        driver.switch_to_default_content()



    # def test_add_bug(self):

    # def tearDown(self):
    #     #每次执行完之后连接数据库执行SQL删除这条
    #     pass


if __name__=="__main__":
    unittest.main()

