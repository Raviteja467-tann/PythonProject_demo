import time

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.utilitis.logger import logger_generator


class basic_login(base_class,locators):
    logger = logger_generator.get_logger("basic login")
    # def __init__(self,driver):
    #     self.driver=driver


    def test_basic_login_function(self,username,password_login):
        self.click(*self.login_home_page)
        self.logger.info("enter username and password")
        self.send_keys(*self.username, username)
        self.send_keys(*self.password, password_login)
        self.click(*self.loginbutton)
        validate_email=self.text(*self.verify_email)
        assert "user467@gmail.com"==validate_email
        self.click(*self.logout)

