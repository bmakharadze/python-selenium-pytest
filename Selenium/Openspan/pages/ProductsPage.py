from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage
from Selenium.Openspan.pages.ProductPage import ProductPage


class ProductsPage(BasePage):
    BEVERAGES_BTN = (By.XPATH, '//*[@id="my-beverages-table"]/tbody/tr[2]/th/a')
    SEASONING_BTN = (By.XPATH, '//*[@id="my-seasonings-table"]/tbody/tr[2]/th/a')

    def __init__(self, driver):
        super().__init__(driver)

    def click_beverages_button(self):
        self.wait_for_element_to_be_visible(self.BEVERAGES_BTN).click()

    def click_seasoning_button(self):
        self.driver.find_element(*self.SEASONING_BTN).click()

    def click_product_button(self, index):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{index}')]").click()
        product_page = ProductPage(self.driver)
        return product_page

    def is_products_page_opened(self):
        return super().is_page_opened(self.BEVERAGES_BTN)
