from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage
from Selenium.Openspan.pages.ProductPage import ProductPage


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.beverages_btn = (By.XPATH, '//*[@id="my-beverages-table"]/tbody/tr[2]/th/a')
        self.seasoning_btn = (By.XPATH, '//*[@id="my-seasonings-table"]/tbody/tr[2]/th/a')

    def click_beverages_button(self):
        self.wait_for_element_to_be_visible(self.beverages_btn).click()

    def click_seasoning_button(self):
        self.driver.find_element(*self.seasoning_btn).click()

    def click_product_button(self, index):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{index}')]").click()
        product_page = ProductPage(self.driver)
        return product_page

    def is_products_page_opened(self):
        return super().is_page_opened(self.beverages_btn)
