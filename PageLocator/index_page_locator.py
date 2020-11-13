#!-*-coding: utf-8 -*-
#!Time  : 2020/11/11 23:56
#!@Author : 张俊彬
from selenium.webdriver.common.by import By


class IndexPageLocator:
    user = (By.XPATH,"//a[text()= '我的帐户[python]']")
    bid = (By.XPATH,"//a[contains(@class ,'btn-specia')]")