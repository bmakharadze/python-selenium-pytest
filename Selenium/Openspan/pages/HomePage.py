from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.product_type = (By.ID, "productType")
        self.product_list = (By.ID, "productsList")
        self.view_products_btn = (By.XPATH, '//*[@id="viewButton"]')

    def select_product_type(self, product_type):
        self.driver.find_element(*self.product_type).send_keys(product_type)

    def select_product_list(self, product_list):
        self.driver.find_element(* self.product_list).send_keys(product_list)

    def click_view_products_button(self):
        self.driver.find_element(*self.view_products_btn).click()

    def is_page_opened(self):
        try:
            self.driver.find_element(*self.view_products_btn)
            return True
        except NoSuchElementException:
            return False, print("Home page not opened")
