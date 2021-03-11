from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # value 替换的变量，类型为字典
    _params = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, locator):
        """
        查找并点击
        :param locator:定位元素
        :return:
        """
        return self.driver.find_element(MobileBy.XPATH, locator).click()

    def find_sendkeys(self, locator, value):
        """
        定位元素并且输入
        :param locator:定位元素
        :param value:键入的内容
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, locator).send_keys(value)

    def swip_click(self, text):
        """
        滑动查找
        :param text: 需要查找的text值
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def wait_click(self, locator):
        """
        显示等待后点击
        :param locator:
        :return:
        """
        element = (MobileBy.XPATH, locator)
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        return ele.click()

    def steps(self, path):
        """
        path -> 路径
        :param path:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            # 读取
            # steps :list[dict]作用跟driver: WebDriver类似，告诉编译器提供对应的方法
            steps = yaml.safe_load(f)
            for step in steps:
                if step["action"] == "find_click":
                    self.find_click(step["locator"])

                if step["action"] == "swip_click":
                    self.swip_click(step["text"])

                if step["action"] == "wait_click":
                    self.wait_click(step["locator"])

                if step["action"] == "find_sendkeys":
                    # value: ”{value}“ --> 可以从python的变量中取值
                    # content: str 提供字符串相关的方法
                    value: str = step["value"]

                    for param in self._params:
                        # 如果里面有指定的”{value}“，替换为现有的变量（现有的变量可以在上面自行定义）
                        # 如果yaml文件中”{value}“命中了_params中的字典中的某一个值时，把字典中的value替换为yaml中的value
                        value = value.replace("{%s}" % param, self._params[param])
                    self.find_sendkeys(step["locator"], value)
