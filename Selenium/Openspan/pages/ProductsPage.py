from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_page_btn = (By.XPATH, '//*[@id="products_menu"]/a')
        self.beverages_btn = (By.XPATH, '//*[@id="my-beverages-table"]/tbody/tr[2]/th/a')
        self.seasoning_btn = (By.XPATH, '//*[@id="my-seasonings-table"]/tbody/tr[2]/th/a')
        '//*[@id="shopping_seasoning_products"]/tbody/tr[1]/td[1]/a[1]'

    def click_products_page_button(self):
        self.driver.find_element(*self.products_page_btn).click()

    def click_beverages_button(self):
        self.driver.find_element(*self.beverages_btn).click()

    def click_seasoning_button(self):
        self.driver.find_element(*self.seasoning_btn).click()

    def click_product_button(self, index):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{index}')]").click()
