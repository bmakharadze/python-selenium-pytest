from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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

    def is_product_page_opened(self):
        return super().is_page_opened(self.order)
