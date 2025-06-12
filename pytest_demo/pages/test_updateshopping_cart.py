import time

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class


class update_shopping_cart:

    def __init__(self,driver):
        self.driver=driver
        self.baseclass=base_class(driver)
        self.element = locators(driver)

    def selectanitem(self):
        self.baseclass.click(*self.element.clickonitem)
        self.baseclass.implicit_wait()
        self.baseclass.click(*self.element.clickonaddtocart)
        time.sleep(3)
        self.baseclass.explicit_wait_visibility_element_located(*self.element.shopping_cart_link)
        self.baseclass.click(*self.element.shopping_cart_link)
        self.baseclass.click(*self.element.cart_items_checkboxes)


    def updateshoppingcartbutton(self):
        self.baseclass.click(*self.element.clickonupdateshoppingcart)
        empty_cart=self.baseclass.text(*self.element.shoppingcartempty)
        assert "Your Shopping Cart is empty!" ==empty_cart