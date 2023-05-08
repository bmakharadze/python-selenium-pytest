from selenium.webdriver.common.by import By

from Selenium.Openspan.base.BasePage import BasePage
from Selenium.Openspan.pages.OrdersPage import OrdersPage
from Selenium.Openspan.pages.ProductPage import ProductPage
from Selenium.Openspan.pages.ProductsPage import ProductsPage


class HomePage(BasePage):
    PRODUCT_TYPE = (By.ID, "productType")
    PRODUCT_LIST = (By.ID, "productsList")
    VIEW_PRODUCTS_BTN = (By.XPATH, '//*[@id="viewButton"]')
    ORDER_MENU_BTN = (By.XPATH, '//*[@id="orders_menu"]/a')
    PRODUCTS_PAGE_BTN = (By.XPATH, '//*[@id="products_menu"]/a')
    ACCOUNT_NAME = (By.XPATH, '//*[@id="user_information_account"]/div[2]/span')

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_menu_button(self):
        self.driver.find_element(*self.ORDER_MENU_BTN).click()
        orders_page = OrdersPage(self.driver)
        return orders_page

    def check_account_status(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def click_products_page_button(self):
        self.driver.find_element(*self.PRODUCTS_PAGE_BTN).click()
        products_page = ProductsPage(self.driver)
        return products_page

    def select_product_type(self, product_type):
        self.driver.find_element(*self.PRODUCT_TYPE).send_keys(product_type)

    def select_product_list(self, product_list):
        self.driver.find_element(*self.PRODUCT_LIST).send_keys(product_list)

    def click_view_products_button(self):
        self.driver.find_element(*self.VIEW_PRODUCTS_BTN).click()
        product_page = ProductPage(self.driver)
        return product_page

    def is_home_page_opened(self):
        return super().is_page_opened(self.PRODUCT_TYPE)
