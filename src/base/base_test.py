import difflib
import pathlib
import mouse

from PIL import ImageChops, Image, ImageGrab
from src.automaton.options import DesktopOptions
from src.automaton import webdriver
# from selenium.webdriver.common.action_chains import ActionChains as AC
# from appium.webdriver.extensions.action_helpers import ActionHelpers


class BaseTest:

    # def __init__(self, driver, exe_path, caps=DesktopOptions()):
    #     self.caps = caps
    #     caps.set_capability("app", exe_path)
    #     caps.set_capability("automationName", "Windows")
    #     caps.set_capability("newCommandTimeout", 60)
    #     self.driver = driver
    #     self.driver.implicitly_wait(5)

    def __init__(self, exe_path, caps=DesktopOptions()):

        self.caps = caps
        caps.set_capability("app", exe_path)
        caps.set_capability("automationName", "Windows")
        caps.set_capability("newCommandTimeout", 60)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=self.caps)
        self.driver.implicitly_wait(5)
        self.mouse = mouse

    def verify(self, obj1, obj2):
        print(f"Verifying: {obj1} vs {obj2}")
        assert obj1 == obj2, ''.join(difflib.ndiff(obj1, obj2))

    # TODO: Work in progress
    def image_compare(self, img) -> str:

        with ImageGrab.grab(all_screens=False).convert("RGB") as image1:
            with Image.open(img).convert("RGB") as image2:
                difference = ImageChops.difference(image1, image2)
                difference.save(str(pathlib.WindowsPath.cwd()) + "\\src\\logs\\screenshots\\diff.png")
                result = str(pathlib.WindowsPath.cwd()) + "\\src\\logs\\screenshots\\diff.png"
        return f"Screenshot saved at location: {result}"

    # Не работает: selenium.common.exceptions.UnknownMethodException: Message: Currently only pen and touch pointer input source types are supported
    # https://githubissues.com/appium/python-client/888
    # def click_on_coords(self, x, y) -> None:
    #     AC(self.driver).move_by_offset(x, y).click().perform()
    #
    # def click_and_hold_on_coords(self, x, y):
    #     AC(self.driver).move_by_offset(x, y).click_and_hold().perform()
    #
    # def release_click(self):
    #     AC(self.driver).release().perform()
