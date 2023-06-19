import time

from selenium.webdriver.common.by import By

from Automation.Amazon.enums.TestData import TestData
from Automation.Amazon.base.BasePage import BasePage
from Automation.Amazon.pages.ProductsPage import ProductsPage


class HomePage(BasePage):
    CHANGE_ADDRESS_BTN = (By.XPATH, '//*[@id="nav-main"]/div[1]/div/div/div[3]/span[2]/span/input')
    CHANGE_ADDRESS_INPUT = (By.XPATH, '//*[@id="GLUXZipUpdateInput"]')
    CHANGE_ADDRESS_APPLY = (By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
    CHANGE_ADDRESS_CONTINUE = (By.XPATH, "//div[@class='a-popover-footer']//input[@id='GLUXConfirmClose']")
    TODAY_DEALS_BTN = (By.XPATH, '//*[@id="nav-xshop"]/a[8]')
    SEARCH_INPUT = (By.XPATH, "//*[@id=\"twotabsearchtextbox\"]")
    SEARCH_BTN = (By.XPATH, "//input[@type='submit']")
    CART_BTN = (By.XPATH,  "//*[@id='nav-cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def change_address(self):
        self.do_click(self.CHANGE_ADDRESS_BTN)
        self.do_send_keys(self.CHANGE_ADDRESS_INPUT, "30303")
        self.do_click(self.CHANGE_ADDRESS_APPLY)
        self.do_click(self.CHANGE_ADDRESS_CONTINUE)

    def click_today_deals_page(self):
        self.do_click(self.TODAY_DEALS_BTN)
        today_deals_page = ProductsPage(self.driver)
        return today_deals_page

    def search_product(self):
        self.do_send_keys(self.SEARCH_INPUT, "laptop")
        self.do_click(self.SEARCH_BTN)
        products_page = ProductsPage(self.driver)
        return products_page

    def is_home_page_opened(self):
        return super().is_page_opened(self.CHANGE_ADDRESS_BTN)
