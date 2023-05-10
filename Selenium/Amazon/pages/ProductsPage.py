import logging

from selenium.webdriver.common.by import By

from Selenium.Amazon.base.BasePage import BasePage
from Selenium.Amazon.pages.ProductPage import ProductPage

logging.basicConfig(level=logging.INFO)


class ProductsPage(BasePage):
    BOOK_BTN = (By.XPATH, "//div[@class='Grid-module__gridDisplayGrid_2X7cDTY7pjoTwwvSRQbt9Y']/div[1]/div/div/a")
    TODAY_DEALS = (By.XPATH, "//*[@id=\"nav-subnav\"]/a[1]/span")
    BOOKS_BTN = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/ul/li[8]/label/input')

    def __init__(self, driver):
        super().__init__(driver)

    def filter_by_books(self):
        self.do_click(self.BOOKS_BTN)

    def click_product(self):
        self.do_click(self.BOOK_BTN)
        product_page = ProductPage(self.driver)
        return product_page

    def filter_by_price(self, price):
        PRODUCT_PRICE = (By.XPATH, f'//span[text()="{price}"]')

        self.do_click(PRODUCT_PRICE)

    def print_all_product_names(self):
        product_elements = self.driver.find_elements(By.XPATH, '//*[@class="a-size-medium a-color-base a-text-normal"]')
        product_names = [element.text for element in product_elements]
        for name in product_names:
            logging.info(f"\n {name}")

    def is_home_page_opened(self):
        return super().is_page_opened(self.TODAY_DEALS)
