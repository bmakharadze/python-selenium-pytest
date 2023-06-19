from selenium.webdriver.common.by import By

from Automation.Amazon.base.BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="add-to-cart-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.do_click(self.ADD_TO_CART_BTN)

    def is_home_page_opened(self):
        return super().is_page_opened(self.ADD_TO_CART_BTN)
