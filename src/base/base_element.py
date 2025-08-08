from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator: str, by_method: str=AppiumBy.NAME, timeout: int = 5) -> WebElement:
        web_element = self.driver.find_element(by_method, locator)
        # wait_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(web_element))
        element = self.driver.create_web_element(list(web_element.values())[0])
        return element

    def click(self, locator: str, by_method: str=AppiumBy.NAME, timeout: int = 5):
        print(f'Click on: {by_method}: {locator}')
        self.element(locator, by_method, timeout).click()

    def attribute(self, locator: str, attribute: str, by_method: str=AppiumBy.NAME, timeout: int = 5) -> str:
        print(f'Get attribute: {by_method}: {locator}')
        return self.element(locator, by_method, timeout).get_attribute(attribute)

    def input(self, locator: str, value: str, by_method: str=AppiumBy.NAME, timeout: int = 5):
        print(f'Input text in: {by_method}: {locator}')
        self.element(locator, by_method, timeout).send_keys(value)

    def text(self, locator: str, by_method: str=AppiumBy.NAME, timeout: int = 5) -> str:
        print(f'Get text from: {by_method}: {locator}')
        return self.element(locator, by_method, timeout).get_attribute("Value.Value")


