from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework.pages.add_info_page import AddInfoPage
from test_appium_homework.pages.basepage import BasePage


class AddMemberPage(BasePage):
    # 跳转到添加联系人详情页
    def add_contact(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.steps("../pages/add_member_page.yaml")

        return AddInfoPage(self.driver)