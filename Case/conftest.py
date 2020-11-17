#!-*-coding: utf-8 -*-
#!Time  : 2020/11/13 12:27
#!@Author : 张俊彬
import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

'''fixture 作用域
fixture的参数中，有scope作用域：
1、function 每个test都会运行，默认值
2、class 每个class的所有test只运行一次
3、module 每个module 的所有test只运行一次
4、session 每个session 只运行一次
'''

from common.readConfig import readConfig
url  = readConfig().getstr('url','url')

@pytest.fixture(scope='class',autouse=True) # autouse=True 自动使用
def fixture_class():
    global driver
    # chrome_options = Options()  #设置无头浏览器
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = Chrome(options=chrome_options, service_log_path=r"D:\ChromeLog\log.log")
    driver = Chrome("D:\Python37\cchromedriver.exe")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def prepara_env() -> None:
    # 前置条件     初始化浏览器
    # driver = Chrome(service_log_path=r"D:\ChromeLog\log.log")
    # driver.maximize_window()
    # driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.get(url)
    yield  driver #分隔符    类似  return
    #后置条件
    driver.refresh()