#!-*-coding: utf-8 -*-
# !Time  : 2020/11/10 22:18
# !@Author : 张俊彬

import win32gui, win32con, time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# PO模式  PageObject
# 原理：
# 将页面的元素定位和元素行为封装成一个page类
# 类的属性：元素定位
# 类的行为：元素操作
# 实现页面对象和测试用例的分离
# 好处：
# 1、档某个也页面元素发生变化，只需要修改该页面中对象的代码即可，测试用例不用修改
# 2、提高代码重用率，结果清晰，维护代码更容易
# 3、测试用例发生变化，不需要或者只需要修改少数页面对象代码
# #
#
from common import constans
from common.myLog import MyLog


class BasePage:
    '''函数注解：括号里面的“:Chrome ”表示参数类型是什么
                括号外面的“-> WebElement”表示返回类型是什么'''
    def __init__(self, driver:Chrome):
        self.driver = driver
        self.mylog = MyLog('元素定位')

    '''等待元素存在，返回找到的元素'''
    def wati_presence_element(self, locator):
        try:
            ele = WebDriverWait(driver=self.driver, timeout=5).until(ec.presence_of_element_located(locator))
            return ele
        except Exception as e:
            self.mylog.error("元素定位失败")
            self.save_screenshot()
            raise e

    '''等待元素可点击，返回找到的要素'''

    def wati_clickable_element(self, locator):
        try:
            ele = WebDriverWait(driver=self.driver, timeout=5).until(ec.element_to_be_clickable(locator))
            return ele
        except Exception as e:
            self.mylog.error("元素定位失败")
            self.save_screenshot()
            raise e

    '''文本框输入'''
    def send_keys(self, locator, data):
        ele = self.wati_presence_element(locator=locator)
        ele.send_keys(data)

    '''点击操作'''
    def click(self, locator):
        ele = self.wati_presence_element(locator=locator)
        ele.click()

    '''获取元素值'''
    def getText(self, locator):
        ele = self.wati_presence_element(locator=locator)
        return ele.text

    '''将窗口滚动到屏幕可见区域'''
    def scrollIntoView(self, locator):
        ele = self.wati_presence_element(locator=locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)


    '''文件上传'''
    def fileLast(self, fileUrl, flag=1):
        try:
            if flag == 1:  # 谷歌浏览器
                dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
            elif flag == 2:  # IE浏览器
                dialog = win32gui.FindWindow("#32770", "选择要加载的文件")  # 一级窗口
        except Exception as e:
            raise e
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级窗口
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)  # 四级窗口
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)  # 二级窗口
        # 操作
        time.sleep(2)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, fileUrl)  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击开始按钮
        time.sleep(2)

    def select_element(self, locator, value, flag=1):
        ele = self.wati_presence_element(locator=locator)
        select = Select(ele)
        if flag == 1:
            select.select_by_index(index=value)
        elif flag == 2:
            select.select_by_value(value=value)
        else:
            select.select_by_visible_text(text=value)

    '''获取Windows弹出窗口text文本'''
    def alert_element(self, flag=None):
        WebDriverWait(self.driver,20).until(ec.alert_is_present())
        alter = self.driver.switch_to.alert
        text = alter.text
        if flag ==1:
            alter.accept()
        elif flag ==2:
            alter.dismiss()
        return  text

    '''移动鼠标到元素上'''
    def actionChains(self,locator):
         ele = self.wati_presence_element(locator=locator)
         action = ActionChains(self.driver)
         action.move_to_element(ele).perform()

    def switch_to_ifram(self,flag, value):
        if flag == 1:
            self.driver.switch_to.frame(value)
        elif flag == 2:
            self.driver.switch_to.frame(value)

    def save_screenshot(self):
        self.driver.save_screenshot(constans.save_image)  # 截屏
    # def switch_handle(self):
    #     handles = self.driver.window_handles
    #     WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it)
