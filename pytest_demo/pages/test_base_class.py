import random
import string

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
# from pytest_demo.conftest import open_browser
#
@pytest.mark.usefixtures("open_browser")
class base_class:

    def __init__(self,driver):
        self.driver=driver

    def random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"testuser_{random_string}@gmail.com"

    def click(self, By, locator):
        click_element=self.driver.find_element(By,locator)
        click_element.click()

    def send_keys(self, By, locator,value):
        send_keys_text=self.driver.find_element(By,locator)
        send_keys_text.send_keys(value)

    def text(self, By, locator):
        # get_text=self.driver.find_element(By, locator)
        # get_text.text()
        return self.driver.find_element(By, locator).text

    def explicit_wait_element_clicable(self,By, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.element_to_be_clickable((By, locator)))

    def explicit_wait_visibility_element_located(self, By, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located((By, locator)))

    def explicit_wait_presence_element_located(self, By, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((By, locator)))

    def implicit_wait(self):
        self.driver.implicitly_wait(5)

