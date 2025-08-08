# C:\Users\User\AppData\Local\Microsoft\WindowsApps\mspaint.exe
import random
import time

import mouse
# import pytest

from appium.webdriver.extensions.action_helpers import ActionHelpers as AH

from src.base.base_test import BaseTest
from src.base.base_element import BaseElement
from src.automaton.windowsby import WindowsBy

from src.automaton import webdriver
from src.automaton.options import DesktopOptions

"""
This file demonstrates a more object-oriented approach.
"""


class TestPaint(BaseTest):

    def __init__(self, exe_path="C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"):
        super().__init__(exe_path)
        self.caps.set_capability("automationName", "Windows")
        self.caps.set_capability("newCommandTimeout", 60)
        self.element = BaseElement(self.driver).element
        self.click = BaseElement(self.driver).click
        self.input = BaseElement(self.driver).input
        self.get_attribute = BaseElement(self.driver).attribute
        self.driver.maximize_window()

    # @pytest.mark.paint
    def _implement_set_canvas_size(self, h=700, w=700):

        self.click("File")
        self.click("Image properties")
        self.click("Width: Minimum1 Maximum99999")
        self.input("Width: Minimum1 Maximum99999", f"{w}")
        self.click("Height: Minimum1 Maximum99999")
        self.input("Height: Minimum1 Maximum99999", f"{h}")
        self.click("//*[@AutomationId='PrimaryButton']", WindowsBy.XPATH)

    def _implement_teardown(self):
        """
        TODO: Создать как фикстуру pytest
        """
        time.sleep(3)
        self.click("File")
        self.click("Exit")
        self.click("//Button[@AutomationId='SecondaryButton']", WindowsBy.XPATH)
        # self.driver.close()

    # @pytest.mark.paint
    def test_paint_canvas_size(self):

        height = random.randrange(50, 1000)
        width = random.randrange(50, 1000)
        expected_result = f"{width} × {height}px"

        self.click("File")
        self.click("Image properties")
        self.click("Width: Minimum1 Maximum99999")
        self.input("Width: Minimum1 Maximum99999", f"{width}")
        self.click("Height: Minimum1 Maximum99999")
        self.input("Height: Minimum1 Maximum99999", f"{height}")
        self.click("//*[@AutomationId='PrimaryButton']", WindowsBy.XPATH)

        result = self.get_attribute("//Text[@AutomationId='CanvasSizeTextBlock']", "Name", WindowsBy.XPATH)
        self.verify(expected_result, result)

        self._implement_teardown()

    def test_paint_on_canvas(self):

        self._implement_set_canvas_size(h=700, w=1000)

        coord_a: tuple = (535, 342)
        coord_b: tuple = (535, 663)
        coord_c: tuple = (600, 342)
        coord_d: tuple = (600, 663)
        coord_f: tuple = (645, 342)
        coord_e: tuple = (555, 342)
        coord_g: tuple = (675, 663)
        coord_h: tuple = (675, 342)
        coord_i: tuple = (740, 342)
        coord_j: tuple = (675, 442)
        coord_k: tuple = (740, 442)
        coord_l: tuple = (780, 342)
        coord_m: tuple = (780, 663)
        coord_n: tuple = (860, 342)
        coord_o: tuple = (860, 442)
        coord_p: tuple = (900, 442)
        coord_q: tuple = (900, 663)

        # Полные пути xPath не всегда работают, как и сокращённые пути.
        # self.click("//*[@ClassName='MSPaintApp']/*[@ClassName='Windows.UI.Composition.DesktopWindowContentBridge']/Pane[@AutomationId='scrollViewer']/Button[@AutomationId='BrushesSplitButton']", WindowsBy.XPATH)

        # Обход - прицелиться в родительский контейнер, так я попал в кнопку "More Options"
        self.click("//*[@ClassName='NamedContainerAutomationPeer'][@Name='Brushes']", by_method=WindowsBy.XPATH)
        self.click("//*[@Name='Marker']", by_method=WindowsBy.XPATH)

        # TODO: создать отдельный метод-утилиту move() -> click() -> drag() -> release()
        def drag_or_draw(x1, y1, x2, y2):
            self.mouse.move(x1, y1)
            self.mouse.click()
            self.mouse.drag(x1, y1, x2, y2, duration=0.4)
            self.mouse.release()

        drag_or_draw(coord_a[0], coord_a[1], coord_b[0], coord_b[1])
        drag_or_draw(coord_c[0], coord_c[1], coord_d[0], coord_d[1])
        drag_or_draw(coord_f[0], coord_f[1], coord_e[0], coord_e[1])
        self.click("Turquoise")
        drag_or_draw(coord_g[0], coord_g[1], coord_h[0], coord_h[1])
        drag_or_draw(coord_h[0], coord_h[1], coord_i[0], coord_i[1])
        drag_or_draw(coord_j[0], coord_j[1], coord_k[0], coord_k[1])
        drag_or_draw(coord_l[0], coord_l[1], coord_m[0], coord_m[1])
        drag_or_draw(coord_l[0], coord_l[1], coord_n[0], coord_n[1])
        drag_or_draw(coord_n[0], coord_n[1], coord_o[0], coord_o[1])
        drag_or_draw(coord_o[0], coord_o[1], coord_p[0], coord_p[1])
        drag_or_draw(coord_p[0], coord_p[1], coord_q[0], coord_q[1])
        drag_or_draw(coord_q[0], coord_q[1], coord_m[0], coord_m[1])


        from src.utilities import screenshot
        screenshot.save_screenshot()
        # self.image_compare('C:\\Users\\User\\PycharmProjects\\desktop-automation\\src\\logs\\screenshots\\screenshot.png')

        self._implement_teardown()


if __name__ == "__main__":
    TestPaint().test_paint_canvas_size()
