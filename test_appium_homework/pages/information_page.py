from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework.pages.address_page import AddressPage
from test_appium_homework.pages.basepage import BasePage

# 主页
class InformationPage(BasePage):
    # 跳转到添加成员页
    def goto_address_list(self):
        self.steps("../pages/information_page.yaml")
        return AddressPage(self.driver)
