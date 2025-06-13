import os
from pytest_demo.pages.test_books_page import Bookspage
from pytest_demo.utilitis.config import url
from pytest_demo.utilitis.logger import logger_generator


class Loginpage(Bookspage):
    logger = logger_generator.get_logger("login method")

    # def __init__(self, driver):
    #     self.driver=driver


    def test_launchurl(self):
        self.driver.get(url)
        self.logger.info("---------launched url----------")
        print("url is opened")

    def login(self,username,password):
        self.logger.info("enter username and password")
        self.send_keys(*self.username, username)
        self.send_keys(*self.password,password)
        self.click(*self.loginbutton)
        try:
            shopping_cart = self.text(*self.shoppingcarttext)
            # print("login Sucessful")
            self.logger.info("-------------sucessfully logged in--------------")
            assert "Shopping cart" in shopping_cart
            # bookspage = Bookspage(self.driver)
            self.test_cart_list_checkbox()
            self.test_checkout()
            self.test_checkout_billing()
        except:
                error_message = self.text(*self.errormesssagetext)
                # if "Login was unsuccessful. Please correct the errors and try again." in error_message:
                print(error_message)
                self.logger.info("------------invalid credentials--------------")
                self.logger.info("------------capture screenshot---------------")
                self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports","login_failed"))
        self.logger.info('----------Login completion-----------')


