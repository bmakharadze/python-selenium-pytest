from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.order = (By.XPATH, '//*[@id="login_button"]')
        self.get_price = (By.XPATH, '//*[@id="home_product_detail"]/tbody/tr/td[2]/p[3]/b')
        self.quantity_select = (By.XPATH, '//*[@name="product_quantity"]')

    def set_quantity(self, index):
        self.driver.find_element(*self.quantity_select).send_keys(index)

    def click_order_button(self):
        self.driver.find_element(*self.order).click()

    def get_price(self):
        element = self.driver.find_element(*self.get_price).text
        print(element)

    def is_page_opened(self):
        try:
            self.driver.find_element(*self.order)
            return True
        except NoSuchElementException:
            return False, print("Product page not opened")
