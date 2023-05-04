from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage
from Selenium.Openspan.pages.HomePage import HomePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id="user_name"]')
        self.password_input = (By.XPATH, '//*[@id="user_pass"]')
        self.login_button = (By.XPATH, '//*[@id="login_button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.wait_for_element_to_be_visible(self.login_button).click()
        home_page = HomePage(self.driver)
        return home_page

    def is_login_page_opened(self):
        return super().is_page_opened(self.username_input)
