#!-*-coding: utf-8 -*-
# !Time  : 2020/11/11 11:26
# !@Author : 张俊彬

from PageObject.login import LoginPage
from PageObject.index import IndexPage
from DataCase.login_datacase import loginDataCase as ld
import pytest

'''实现pytest
1、随机测试
2、测试环境管理 fixture
3、测试用例发现
4、测试报告生成  allure
5、冲运行机制'''
'''
mark 随机运行某一些测试用例
mark 可以放到方法上，也可以放到类上面
一个方法和类可以加多个标签
注意：mark 表达式 一定要用双引号
    清理缓存文件，缓存文件夹
2、跳过函数
3、自动发现测试
4、断言方便
5、插件丰富，重运行、allure
6、兼容unittest ,如同时使用pytest参数化会导致不兼容
7、fixture 环境管理灵活
'''


@pytest.mark.usefixtures('prepara_env')
class TestLogin:
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('item', ld.data_case)
    def test_login_3_success(self, item, prepara_env):
        LoginPage(driver=prepara_env).login(item['user'], item['pwd'])
        ele_text = IndexPage(prepara_env).get_user_info()
        try:
            assert ele_text == item['Expected']
        except AssertionError as e:
            raise e

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('item', ld.data_exception)
    def test_login_2_exception(self, item, prepara_env):
        LoginPage(driver=prepara_env).login(item['user'], item['pwd'])
        ele_text = LoginPage(driver=prepara_env).get_error1_message()
        try:
            assert ele_text == item['Expected']
        except AssertionError as e:
            raise e

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize('item',ld.data_error,)
    def test_login_1_error(self, item,prepara_env):
        LoginPage(driver=prepara_env).login(item['user'], item['pwd'])
        ele_text = LoginPage(driver=prepara_env).get_error_message()
        try:
            assert ele_text == item['Expected']
        except AssertionError as e:
            raise e


if __name__ == '__main__':
    pass
