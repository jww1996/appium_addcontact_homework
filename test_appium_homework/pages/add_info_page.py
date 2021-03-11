from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework.pages.basepage import BasePage


# 添加通讯录信息

class AddInfoPage(BasePage):
    # 添加联系人
    def add_info(self, username, phone_num):
        """
        1.添加联系人姓名
        2.选择性别
        3.添加手机号码
        4.点击保存
        :param username:
        :param phone_num:
        :return:
        """
        self._params["name"] = username
        self._params["number"] = phone_num
        self.steps("../pages/add_info_page.yaml")
        # print(self.driver.page_source)
        # 获取toast的text值
        add_result = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"添加成功")]').text
        return add_result
