#!-*-coding: utf-8 -*-
# !Time  : 2020/11/11 11:26
# !@Author : 张俊彬
import unittest
from ddt import ddt, data
from selenium.webdriver import Chrome
from PageObject.login import LoginPage
from PageObject.index import IndexPage
from DataCase.login_datacase import loginDataCase as ld

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#只会执行一次
        cls.driver = Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://120.78.128.25:8765/Index/login.html')
        cls.login_page = LoginPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self) -> None: #每次执行用例前执行
        # # 初始浏览器
        # self.driver = Chrome()
        # self.driver.maximize_window()
        # # 访问登录页面
        # self.driver.get('http://120.78.128.25:8765/Index/login.html')
        # self.login_page = LoginPage(self.driver)
        pass

    def tearDown(self) -> None:
        # self.driver.quit()
        self.driver.refresh()
        pass

    @data(*ld.data_case)
    def test_login_3_success(self,item):
        self.login_page.login(item['user'],item['pwd'])
        ele_text = IndexPage(self.driver).get_user_info()
        try:
            self.assertEqual(ele_text,item['Expected'])
        except AssertionError as e:
            raise

    @data(*ld.data_exception)
    def test_login_2_exception(self,item):
        #请输入密码   请输入手机号
        self.login_page.login(item['user'], item['pwd'])
        ele_text = self.login_page.get_error1_message()
        try:
            self.assertEqual(ele_text, item['Expected'])
        except AssertionError as e:
            raise e

    @data(*ld.data_error)
    def test_login_1_error(self, item):
        #帐号或密码错误!    此账号没有经过授权，请联系管理员!
        self.login_page.login(item['user'], item['pwd'])
        ele_text = self.login_page.get_error_message()
        try:
            self.assertEqual(ele_text, item['Expected'])
        except AssertionError as e:
            raise e
if __name__ == '__main__':
    # 运行整个测试类
    unittest.main()