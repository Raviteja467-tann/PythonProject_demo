import time

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.utilitis.logger import logger_generator


class basic_login:
    logger = logger_generator.get_logger("basic login")
    def __init__(self,driver):
        self.driver=driver
        self.baseclass=base_class(driver)
        self.element = locators(driver)

    def test_basic_login_function(self,username,password_login):
        self.baseclass.click(*self.element.login_home_page)
        self.logger.info("enter username and password")
        self.baseclass.send_keys(*self.element.username, username)
        self.baseclass.send_keys(*self.element.password, password_login)
        self.baseclass.click(*self.element.login)
        validate_email=self.baseclass.text(*self.element.verify_email)
        assert "user467@gmail.com"==validate_email
        self.baseclass.click(*self.element.logout)

