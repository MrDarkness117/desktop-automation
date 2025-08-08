import subprocess
import time
import difflib

import pycountry
import locale

from src.automaton import webdriver
from src.automaton.options import DesktopOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys

"""
This file demonstrates a basic example of how to use the webdriver's locators to work with UI elements.
"""

caps = DesktopOptions()
caps.set_capability("app","C:\\Windows\\System32\\notepad.exe")

caps.set_capability("automationName", "Windows")
caps.set_capability("newCommandTimeout", 60)

pscmd = 'Set-WinUserLanguageList'
subprocess.Popen(['powershell', '-Command', f'{pscmd} en-US -force'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=caps)

with open("../example", "r", encoding='cp1251') as f:
    content = f.readlines()

driver.implicitly_wait(30)
elm = driver.find_element(AppiumBy.NAME, "Text editor")
editor = driver.create_web_element(list(elm.values())[0])
text = '\n'.join(content)
editor.send_keys(text)
# for line in content:
#     editor.send_keys(line)
#     if not line == content[-1]:
#         editor.send_keys(Keys.RETURN)
driver.create_web_element(list(driver.find_element(AppiumBy.NAME, "Edit").values())[0]).click()
driver.create_web_element(list(driver.find_element(AppiumBy.NAME, "Font").values())[0]).click()
time.sleep(1)
driver.create_web_element(list(driver.find_element(AppiumBy.ACCESSIBILITY_ID, "FontFamilyComboBox").values())[0]).click()
driver.create_web_element(list(driver.find_element(AppiumBy.ACCESSIBILITY_ID, "FontFamilyComboBox").values())[0]).send_keys("Calibri")
time.sleep(1)
editor.send_keys(Keys.RETURN)
driver.create_web_element(list(driver.find_element(AppiumBy.NAME, "Back").values())[0]).click()
assert editor.get_attribute("Value.Value") == content, ''.join(difflib.ndiff(content, editor.text))
driver.create_web_element(list(driver.find_element(AppiumBy.NAME, "File").values())[0]).click()
driver.create_web_element(list(driver.find_element(AppiumBy.NAME, "Exit").values())[0]).click()

# FIXME: The command must set languages back, instead it sets langauge to ru-RU
subprocess.Popen(['powershell', '-Command', f'{pscmd}', '-languagelist', 'ru-RU,en-EN',  '-force'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

with open("../example", "r", encoding='cp1251') as f:
    content=f.read()

driver.close()


   
 
