#from pytest_demo.conftest import open_browser
from pytest_demo.pages.test_basic_login_function import basic_login
from pytest_demo.pages.test_login_page import Loginpage
from pytest_demo.utilitis.config import username, password_login


def test_basic_login(open_browser):
    driver = open_browser
    loginpage = Loginpage(driver)
    loginpage.test_launchurl()
    basiclogin=basic_login(driver)
    basiclogin.test_basic_login_function(username,password_login)