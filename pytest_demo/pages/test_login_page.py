import os
from logging import exception

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.pages.test_books_page import Bookspage
from pytest_demo.utilitis.config import url
from pytest_demo.utilitis.logger import logger_generator


class Loginpage:
    logger = logger_generator.get_logger("login method")

    def __init__(self, driver):
        self.driver=driver
        self.baseclass=base_class(driver)
        self.element = locators(driver)

    def test_launchurl(self):
        self.driver.get(url)
        self.logger.info("---------launched url----------")
        print("url is opened")

    def login(self,username,password):
        self.logger.info("enter username and password")
        self.baseclass.send_keys(*self.element.username, username)
        self.baseclass.send_keys(*self.element.password,password)
        self.baseclass.click(*self.element.login)
        try:
            shopping_cart = self.baseclass.text(*self.element.shoppingcarttext)
            # print("login Sucessful")
            self.logger.info("-------------sucessfully logged in--------------")
            assert "Shopping cart" in shopping_cart
            bookspage = Bookspage(self.driver)
            bookspage.test_cart_list_checkbox()
            bookspage.test_checkout()
            bookspage.test_checkout_billing()
        except:
                error_message = self.baseclass.text(*self.element.errormesssagetext)
                # if "Login was unsuccessful. Please correct the errors and try again." in error_message:
                print(error_message)
                self.logger.info("------------invalid credentials--------------")
                self.logger.info("------------capture screenshot---------------")
                self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports","login_failed"))
        self.logger.info('----------Login completion-----------')


