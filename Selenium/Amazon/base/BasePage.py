from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_page_opened(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logging.info("Page is opened.")
            return element
        except TimeoutException:
            logging.info("Page is not opened.")

    def wait_for_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_for_element_to_be_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
