import pytest

from pytest_demo.pages.test_books_page import Bookspage
from pytest_demo.pages.test_login_page import Loginpage
from pytest_demo.pages.test_search_homepage import Homepage_search
from pytest_demo.conftest import open_browser
from pytest_demo.utilitis.login_data_excel import readdata_excel


@pytest.mark.parametrize("username,password",readdata_excel())
def test_search_box(open_browser,username,password):
    driver= open_browser
    loginpage = Loginpage(driver)
    loginpage.test_launchurl()
    search = Homepage_search(driver)
    search.test_search()
    loginpage.login(username, password)