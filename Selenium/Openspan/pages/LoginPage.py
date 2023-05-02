from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id="user_name"]')
        self.password_input = (By.XPATH, '//*[@id="user_pass"]')
        self.login_button = (By.XPATH, '//*[@id="login_button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        login = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button))
        assert login.is_displayed(), "Login button is not displayed."
        login.click()

    def is_page_opened(self):
        try:
            self.driver.find_element(*self.username_input)
            return True
        except NoSuchElementException:
            return False, print("Login page not opened")
