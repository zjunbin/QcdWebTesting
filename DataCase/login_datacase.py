#!-*-coding: utf-8 -*-
#!Time  : 2020/11/12 0:21
#!@Author : 张俊彬
class loginDataCase:
    data_case= [{"user":"18684720553","pwd":"python","Expected":"我的帐户[python]"}]
    data_exception =[{"user":"18684720333","pwd":"","Expected":"请输入密码"},
                     {"user": "", "pwd": "python", "Expected": "请输入手机号"},
                     {"user": "186847205531", "pwd": "python", "Expected": "请输入正确的手机号"},
                     {"user": "1868472055", "pwd": "python", "Expected": "请输入正确的手机号"},
                     {"user": "", "pwd": "", "Expected": "请输入手机号"}]
    data_error = [{"user":"18684720553","pwd":"1234567","Expected":"帐号或密码错误!"},
                  {"user": "17684720553", "pwd": "123456", "Expected": "此账号没有经过授权，请联系管理员!"}]
