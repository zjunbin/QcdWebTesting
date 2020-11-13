#!-*-coding: utf-8 -*-
#!Time  : 2020/11/11 16:54
#!@Author : 张俊彬
from PageLocator.login_page_locator import loginPageLocator as ll
from common.BasePage import BasePage


class LoginPage(BasePage):
    def login(self,username,pwd):
        # 1、打开浏览器# 访问登录页面
        # 3.定位元素
        # 4.发送登录用户名和密码
        # 5.断言
        #"18684720553""python")
        self.send_keys(ll.userName,username)
        self.send_keys(ll.txtPass,pwd)
        self.click(ll.loginBtn)
        return self.driver
    def get_error1_message(self):
        ele_text = self.getText(ll.error1)
        return ele_text
    def get_error_message(self):
        ele_text = self.getText(ll.error)
        return ele_text
