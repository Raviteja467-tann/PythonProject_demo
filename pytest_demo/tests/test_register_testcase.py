from pytest_demo.pages.test_login_page import Loginpage
from pytest_demo.pages.test_register_page import Register
from pytest_demo.conftest import open_browser


def test_register_testcase(open_browser):
    driver = open_browser
    loginpage = Loginpage(driver)
    loginpage.test_launchurl()
    register = Register(driver)
    register.test_register_page()
    register.test_registration_page()
