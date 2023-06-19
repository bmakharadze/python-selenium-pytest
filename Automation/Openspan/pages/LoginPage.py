from selenium.webdriver.common.by import By

from Automation.Openspan.base.BasePage import BasePage
from Automation.Openspan.enums.TestData import TestData
from Automation.Openspan.pages.HomePage import HomePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id="user_name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="user_pass"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self, username, password):
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.do_click(self.LOGIN_BUTTON)
        home_page = HomePage(self.driver)
        return home_page

    def is_login_page_opened(self):
        return self.is_visible(self.USERNAME_INPUT)
