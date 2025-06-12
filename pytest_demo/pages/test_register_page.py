import os
import time

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.utilitis.config import firstname, lastname, password, confirmpassword
from pytest_demo.utilitis.logger import logger_generator


class Register:
    logger=logger_generator.get_logger("Register page")
    def __init__(self,driver):
        self.driver=driver
        self.baseclass=base_class(driver)
        self.element=locators(driver)
        self.driver.implicitly_wait(5)


    def test_register_page(self):
        self.logger.info("----------click on register link---------")
        self.baseclass.click(*self.element.register_link)

    def test_registration_page(self):
        #self.driver.find_element(By.XPATH,personal_details+"//input[@id='gender-male']").click()
        self.logger.info("----------pass the required details in to register page---------")
        self.baseclass.click(*self.element.male)
        self.baseclass.send_keys(*self.element.firstname,firstname)
        self.baseclass.send_keys(*self.element.lastname,lastname)
        self.baseclass.send_keys(*self.element.registrationemail, self.baseclass.random_email())
        self.baseclass.send_keys(*self.element.registrationpassword,password)
        self.baseclass.send_keys(*self.element.registrationconfirmpassword, confirmpassword)
        self.baseclass.click(*self.element.registrationsubmitbutton)
        complete_text=self.baseclass.text(*self.element.completedtext)
        self.logger.info("-------------registration sucessful---------------")
        print(complete_text)
        self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports","test_registration"))
        time.sleep(2)
        assert "Your registration completed" == complete_text

