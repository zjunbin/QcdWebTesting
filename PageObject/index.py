#!-*-coding: utf-8 -*-
#!Time  : 2020/11/11 23:53
#!@Author : 张俊彬
from common.BasePage import BasePage
from PageLocator.index_page_locator import IndexPageLocator as il
class IndexPage(BasePage):
    def get_user_info(self):
        user_element = self.wati_presence_element(il.user)
        return user_element.text

    def chose_bid(self):
        self.wati_clickable_element(il.bid)
