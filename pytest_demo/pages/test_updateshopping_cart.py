import time

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class


class update_shopping_cart(base_class, locators):

    # def __init__(self,driver):
    #     self.driver=driver

    def selectanitem(self):
        self.click(*self.clickonitem)
        self.implicit_wait()
        self.click(*self.clickonaddtocart)
        time.sleep(3)
        self.explicit_wait_visibility_element_located(*self.shopping_cart_link)
        self.click(*self.shopping_cart_link)
        self.click(*self.cart_items_checkboxes)


    def updateshoppingcartbutton(self):
        self.click(*self.clickonupdateshoppingcart)
        empty_cart=self.text(*self.shoppingcartempty)
        assert "Your Shopping Cart is empty!" ==empty_cart