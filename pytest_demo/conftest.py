import os.path
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest_demo.pages.test_books_page import Bookspage

driver=None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="run slow tests"
    )
@pytest.fixture(scope="function")
def open_browser(request):
    global driver
    try:
        browser_name = request.config.getoption("browser_name")
    except (AttributeError, ValueError):
        browser_name = "Chrome"
    if browser_name == "Chrome":
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
    elif browser_name == "Firefox":
        driver=webdriver.Firefox()
        driver.maximize_window()
    elif browser_name == "Ie":
        driver=webdriver.Ie()
        driver.maximize_window()


    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            #file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            time.sleep(2)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)