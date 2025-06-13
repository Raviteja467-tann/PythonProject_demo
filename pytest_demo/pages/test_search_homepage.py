import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing_extensions import KeysView

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.pages.test_books_page import Bookspage
from pytest_demo.pages.test_login_page import Loginpage
from pytest_demo.utilitis.logger import logger_generator


class Homepage_search(Bookspage):
    logger = logger_generator.get_logger("login method")
    # def __init__(self, driver):
    #     self.driver = driver

    def test_search(self):
        text=self.explicit_wait_element_clicable(*self.search_box)
        self.logger.info("-----------passing the text in to search box------------")
        text.send_keys("phon")
        search_options = self.driver.find_elements(*self.searchoptionslist)
        for dropdown_text in search_options:
            print(dropdown_text.text)
            text.send_keys(Keys.ARROW_DOWN)
            if dropdown_text.text=="Phone Cover":
                text.send_keys(Keys.ENTER)
                self.logger.info("-----------passed the text and entered using keys----------")
                break
        time.sleep(2)
        addtocart=self.explicit_wait_element_clicable(*self.addtocart)
        addtocart.click()
        time.sleep(2)
        shoppingcart = self.explicit_wait_element_clicable(*self.shopping_cart_link)
        shoppingcart.click()
        self.click(*self.shoppingcartcheckbox)
        self.click(*self.terms_condition)
        self.test_checkout()



