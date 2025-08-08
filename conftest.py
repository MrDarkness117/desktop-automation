# import pytest
from src.automaton import webdriver
from src.automaton.options import DesktopOptions
from src.base.base_element import BaseElement
from src.base.base_test import BaseTest


# def pytest_addoption(parser):
#     parser.addoption("--app", help="")
#
# def pytest_generate_tests(metafunc):
#     if metafunc.config.getoption("app"):


@pytest.fixture()
def setup(exe_path="C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"):
    caps = DesktopOptions()
    caps.set_capability("app", exe_path)
    caps.set_capability("automationName", "Windows")
    caps.set_capability("newCommandTimeout", 60)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps)
    yield driver
