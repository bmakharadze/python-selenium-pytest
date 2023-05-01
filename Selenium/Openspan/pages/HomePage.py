from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def select_product_type(self, product_type):
        self.driver.find_element(By.ID, "productType").send_keys(product_type)

    def select_product_list(self, product_list):
        self.driver.find_element(By.ID, "productsList").send_keys(product_list)

    def click_view_products_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="viewButton"]').click()
