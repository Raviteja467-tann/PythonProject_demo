#from pytest_demo.conftest import open_browser
from pytest_demo.pages.test_login_page import Loginpage
from pytest_demo.pages.test_updateshopping_cart import update_shopping_cart


def test_updatecart(open_browser):
    driver=open_browser
    loginpage = Loginpage(driver)
    loginpage.test_launchurl()
    updatecart=update_shopping_cart(driver)
    updatecart.selectanitem()
    updatecart.updateshoppingcartbutton()
