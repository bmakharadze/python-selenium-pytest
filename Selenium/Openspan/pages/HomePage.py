from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage
from Selenium.Openspan.pages.OrdersPage import OrdersPage
from Selenium.Openspan.pages.ProductPage import ProductPage
from Selenium.Openspan.pages.ProductsPage import ProductsPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_type = (By.ID, "productType")
        self.product_list = (By.ID, "productsList")
        self.view_products_btn = (By.XPATH, '//*[@id="viewButton"]')
        self.order_menu_btn = (By.XPATH, '//*[@id="orders_menu"]/a')
        self.products_page_btn = (By.XPATH, '//*[@id="products_menu"]/a')

    def click_order_menu_button(self):
        self.driver.find_element(*self.order_menu_btn).click()
        orders_page = OrdersPage(self.driver)
        return orders_page

    def click_products_page_button(self):
        self.driver.find_element(*self.products_page_btn).click()
        products_page = ProductsPage(self.driver)
        return products_page

    def select_product_type(self, product_type):
        self.driver.find_element(*self.product_type).send_keys(product_type)

    def select_product_list(self, product_list):
        self.driver.find_element(* self.product_list).send_keys(product_list)

    def click_view_products_button(self):
        self.driver.find_element(*self.view_products_btn).click()
        product_page = ProductPage(self.driver)
        return product_page

    def is_home_page_opened(self):
        return super().is_page_opened(self.productType)
