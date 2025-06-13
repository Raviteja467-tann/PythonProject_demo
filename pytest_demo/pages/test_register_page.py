import os
import time

from selenium.webdriver.common.by import By

from pytest_demo.locators.locators import locators
from pytest_demo.pages.test_base_class import base_class
from pytest_demo.utilitis.config import firstname, lastname, password, confirmpassword
from pytest_demo.utilitis.logger import logger_generator


class Register(base_class,locators):
    logger=logger_generator.get_logger("Register page")
    # def __init__(self,driver):
    #     self.driver=driver



    def test_register_page(self):
        self.logger.info("----------click on register link---------")
        self.click(*self.register_link)

    def test_registration_page(self):
        #self.driver.find_element(By.XPATH,personal_details+"//input[@id='gender-male']").click()
        self.logger.info("----------pass the required details in to register page---------")
        self.click(*self.male)
        self.send_keys(*self.firstname,firstname)
        self.send_keys(*self.lastname,lastname)
        self.send_keys(*self.registrationemail, self.random_email())
        self.send_keys(*self.registrationpassword,password)
        self.send_keys(*self.registrationconfirmpassword, confirmpassword)
        self.click(*self.registrationsubmitbutton)
        complete_text=self.text(*self.completedtext)
        self.logger.info("-------------registration sucessful---------------")
        print(complete_text)
        self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports","test_registration"))
        time.sleep(2)
        assert "Your registration completed" == complete_text

