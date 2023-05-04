from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def is_page_opened(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info("Page is opened.")
            return element
        except TimeoutException:
            self.logger.info("Page is not opened.")

    def wait_for_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_for_element_to_be_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element
