from appium.webdriver.common.mobileby import MobileBy

from test_appium_homework.pages.add_member_page import AddMemberPage
from test_appium_homework.pages.basepage import BasePage


class AddressPage(BasePage):
    # 滑动查找，跳转到手动添加联系人页
    def goto_add_contact(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.steps("../pages/address_page.yaml")
        return AddMemberPage(self.driver)
