import pytest
from selenium import webdriver
import logging

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Configure the logging module
logging.basicConfig(level=logging.INFO)


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    logging.info(" Setting up driver...")
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()
