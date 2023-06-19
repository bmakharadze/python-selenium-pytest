import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Automation.Openspan.enums.TestData import TestData
from Automation.Openspan.pages.LoginPage import LoginPage


@pytest.fixture(scope="module", params=["chrome"])
def init_driver(request):
    logging.info("Setting up driver...")
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://training.openspan.com/login")

    # For every test, it is needed to be logged in to the website
    login_page = LoginPage(driver)
    assert login_page.is_login_page_opened(), "Login page is not opened."
    login_page.login(TestData.ACCOUNT_NAME, TestData.ACCOUNT_PASSWORD)
    login_page.click_login_button()

    yield driver
    driver.quit()
