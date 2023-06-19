from selenium.webdriver.common.by import By

from Automation.Openspan.base.BasePage import BasePage


class ProductPage(BasePage):
    ORDER = (By.XPATH, '//*[@id="login_button"]')
    GET_PRICE = (By.XPATH, '//*[@id="home_product_detail"]/tbody/tr/td[2]/p[3]/b')
    QUANTITY_SELECT = (By.XPATH, '//*[@name="product_quantity"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_quantity(self, index):
        self.driver.find_element(*self.QUANTITY_SELECT).send_keys(index)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER).click()

    def get_price(self):
        element = self.driver.find_element(*self.GET_PRICE).text
        print(element)

    def is_product_page_opened(self):
        return super().is_page_opened(self.ORDER)
