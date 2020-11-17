#!-*-coding: utf-8 -*-
#!Time  : 2020/11/13 0:42
#!@Author : 张俊彬
import pytest
from common import constans
if __name__ == '__main__':
    pytest.main(['-m smoke','-s',r'--html=result/{}',r'--alluredir={}'.format(constans.html_path,constans.allure_paht)])