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


class Homepage_search:
    logger = logger_generator.get_logger("login method")
    def __init__(self,driver):
        self.driver = driver
        self.baseclass=base_class(driver)
        self.bookspage = Bookspage(driver)
        self.element=locators(driver)

    def test_search(self):

        # text=self.driver.find_element(*self.search_box)
        # text.send_keys("cel")
        # wait= WebDriverWait(self.driver,5)
        # text =wait.until(expected_conditions.element_to_be_clickable(self.element.search_box))
        text=self.baseclass.explicit_wait_element_clicable(*self.element.search_box)
        self.logger.info("-----------passing the text in to search box------------")
        text.send_keys("phon")
        search_options = self.driver.find_elements(*self.element.searchoptionslist)
        for dropdown_text in search_options:
            print(dropdown_text.text)
            text.send_keys(Keys.ARROW_DOWN)
            if dropdown_text.text=="Phone Cover":
                text.send_keys(Keys.ENTER)
                self.logger.info("-----------passed the text and entered using keys----------")
                break
        # self.driver.find_element(By.XPATH,"//input[@class='button-1 search-box-button']").click()
        time.sleep(2)
        # add_to_cart_xpath=(By.XPATH,"//input[@value='Add to cart']")
        # wait = WebDriverWait(self.driver, 5)
        # addtocart = wait.until(expected_conditions.element_to_be_clickable(self.element.addtocart))
        addtocart=self.baseclass.explicit_wait_element_clicable(*self.element.addtocart)
        addtocart.click()
        time.sleep(2)
        # wait = WebDriverWait(self.driver, 5)
        shoppingcart = self.baseclass.explicit_wait_element_clicable(*self.element.shopping_cart_link)
        shoppingcart.click()
        self.baseclass.click(*self.element.shoppingcartcheckbox)
        self.baseclass.click(*self.element.terms_condition)
        self.bookspage.test_checkout()



