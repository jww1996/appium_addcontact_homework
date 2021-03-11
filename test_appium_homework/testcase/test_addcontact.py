from typing import List, Dict

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework.pages.app import App
from test_appium_homework.pages.information_page import InformationPage
import random


class TestAddContact:
    def setup(self):

        self.app = App()

    def test_add_contact(self):
        # 从testcase中读取联系人的姓名，电话，赋值给username，
        with open("../pages/testdatas.yaml", encoding="utf-8") as f:
            steps: List[Dict] = yaml.safe_load(f)
            for step in steps:
                if "name" in step.keys():
                    username = step["name"]
                if "number" in step.keys():
                    phone_num = step["number"]
        # 获取随机数
        # n1 = random.randint(0, 9)
        # num = random.randint(11111111, 99999999)
        #
        # # 将要添加的成员信息
        # username = f'name_{n1}'
        # phone_num = f'136{num}'

        add_result = self.app.goto_main().goto_address_list().goto_add_contact().add_contact().add_info(username, phone_num)
        # 断言 是否添加成功
        assert "添加成功" == add_result
