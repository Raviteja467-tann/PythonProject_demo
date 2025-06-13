import pytest

from pytest_demo.conftest import open_browser
from pytest_demo.pages.test_books_page import Bookspage
from pytest_demo.utilitis.login_data_excel import readdata_excel
from pytest_demo.pages.test_login_page import Loginpage


@pytest.mark.parametrize("username,password",readdata_excel())
def test_url(open_browser,username,password):
    driver= open_browser
    loginpage = Loginpage(driver)
    bookspage = Bookspage(driver)
    loginpage.test_launchurl()
    bookspage.test_book()
    bookspage.test_cart_list_checkbox()
    bookspage.test_checkout()
    loginpage.login(username, password)




