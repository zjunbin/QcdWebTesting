#!-*-coding: utf-8 -*-
#!Time  : 2020/11/11 16:25
#!@Author : 张俊彬
from selenium.webdriver.common.by import By


class loginPageLocator:
    userName = (By.XPATH,"//input[@name = 'phone']")
    txtPass = (By.XPATH,"//input[@name = 'password']")
    loginBtn = (By.XPATH,"//button[@type = 'button']")

    #请输入手机号 \ 请输入密码
    error1 = (By.XPATH,"//div[@class = 'form-error-info']")
    #用户名或密码错误
    error = (By.XPATH,"//*[@class= 'layui-layer-content']")