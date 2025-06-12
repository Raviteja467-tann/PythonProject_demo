import os

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.utilitis.config import url
from pytest_demo.utilitis.logger import logger_generator


#@pytest.mark.usefixtures("open_browser")
class Bookspage:
    logger = logger_generator.get_logger("Books page")
    def __init__(self, driver):
        self.driver=driver
        self.baseclass = base_class(driver)
        self.element = locators(driver)

    def test_launchurl(self):
        self.driver.get(url)
        self.logger.info("-----------url launched----------")
        print("url is opened")


    def test_book(self):
        self.baseclass.click(*self.element.book)
        self.logger("---------fetch list of book items-----------")
        books_list=self.driver.find_elements(*self.element.books_list)
        book_data = []
        #taking the list of book items on the page
        for books in books_list:
            #taking the books name from the book items
                books_name= books.find_element(By.XPATH,"./div//h2/a")
            #using try except because if add to cart button is not there it will not stop further steps
                try:
                    #taking the add to cart button from the book items
                    add_to_cart_button=books.find_element(*self.element.addtocart)
                    cart_button=add_to_cart_button.get_attribute("value")
                    # add to cart button is there, then only it will go to this if block
                    if "Add to cart" in cart_button:
                        #created a empty list and appending the data for sorting
                        book_data.append(books_name.text)
                        #print(book_data)
                        add_to_cart_button.click()
                except :
                    print("Add to cart button is not found for the "+books_name.text)
        #once the data is append sorting the data
        book_data.sort()
        self.logger.info("---------sorted list of books----------")
        print(book_data)
        self.driver.find_element(*self.element.shopping_cart_link).click()
        cart_books_data = []
        #after adding to cart, validating the books which are showing in cart are selected books or not
        books_cart_list = self.driver.find_elements(*self.element.booksincartlist)
        for cart_books in books_cart_list:
            cart_books_data.append(cart_books.text)
        cart_books_data.sort()
        self.logger.info("------------sorted list of books in cart-----------")
        print(cart_books_data)
        assert cart_books_data==book_data
        self.logger.info("------------books data is matched--------------")

    def test_cart_list_checkbox(self):
        cart_items= self.driver.find_elements(*self.element.cart_items_checkboxes)
        for checkboxitems in cart_items:
            checkboxitems.click()
        self.logger.info("-----------selected check boxes in the cart which are added to cart---------------")
        self.driver.find_element(*self.element.terms_condition).click()

    def test_checkout(self):
        self.logger.info("-----------click on the check out button------------")
        self.driver.find_element(*self.element.submit_button).click()

    def test_checkout_billing(self):
        self.logger.info("-----------landed on the billing page---------------")
        self.baseclass.click(*self.element.billingsave)
        self.baseclass.click(*self.element.shippingsave)
        self.baseclass.click(*self.element.shippingmethodsave)
        self.baseclass.click(*self.element.paymentmethodsave)
        self.baseclass.click(*self.element.paymentinfosave)
        self.baseclass.click(*self.element.confirmorder)
        succcess_message= self.baseclass.text(*self.element.successmessagetext)
        print(succcess_message)
        self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports","successfully added to cart"))
        self.baseclass.click(*self.element.ordercompleted)
        self.baseclass.click(*self.element.logout)
        self.logger.info("------------Logged out sucessfully---------------")







