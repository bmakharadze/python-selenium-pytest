from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class OrdersPage:
    def __init__(self, driver):
        self.driver = driver
        self.order_menu_btn = (By.XPATH, '//*[@id="orders_menu"]/a')
        self.next_btn = (By.XPATH, '//*[@id="next1_button"]')
        self.step_2_next_button = (By.XPATH, '//*[@id="next2_button"]')
        self.step_2_previous_button = (By.XPATH, '"//*[@name="previous"]"')
        self.credit_card = (By.XPATH, '//*[@id="credit_card"]')
        self.bill_me = (By.XPATH, '//*[@id="bill_me"]')
        self.order_number = (By.XPATH, '//*[@id="purchase_order_number"]')
        self.step_3_submit_button = (By.XPATH, '//*[@id="submit_button"]')
        self.step_3_previous_button = (By.XPATH, '//*[@id="progressbar_container"]/fieldset[3]/input[1]')
        self.verify_credit_limit = (By.ID, 'verify_credit_limit')

    def click_order_menu_button(self):
        self.driver.find_element(*self.order_menu_btn).click()

    def click_next_button(self):
        self.driver.find_element(*self.next_btn).click()

    # STEP 2
    def placeOrderStep2(self, first_name, last_name, street_address, zip_code, area_code, phone):
        first_name_input = "//input[@id='bfirst_name']"
        last_name_input = "//input[@name='blast_name']"
        street_address_input = "//*[@id='bstreet_address']"
        zip_code_input = "//*[@id='bzip_code']"
        area_code_input = "//input[contains(@placeholder, 'Area')]"
        primary_phone_input = "//*[@id='bprimary_phone']"
        ship_to_billing_address_btn = "//*[contains(text(), 'Ship to')]"

        self.driver.find_element(By.XPATH, first_name_input).send_keys(first_name)
        self.driver.find_element(By.XPATH, last_name_input).send_keys(last_name)
        self.driver.find_element(By.XPATH, street_address_input).send_keys(street_address)
        self.driver.find_element(By.XPATH, zip_code_input).send_keys(zip_code)
        self.driver.find_element(By.XPATH, area_code_input).send_keys(area_code)
        self.driver.find_element(By.XPATH, primary_phone_input).send_keys(phone)
        self.driver.find_element(By.XPATH, ship_to_billing_address_btn).click()

    def click_step_2_next_button(self):
        self.driver.find_element(*self.step_2_next_button).click()

    def click_step_2_previous_button(self):
        self.driver.find_element(*self.step_2_previous_button).click()

    # STEP 3
    def click_credit_card_button(self):
        self.driver.find_element(*self.credit_card).click()

    def click_bill_me_button(self):
        self.driver.find_element(*self.bill_me).click()

    def placeOrderStep3(self, card_type, security_code, card_number, expiration_month, expiration_year):
        self.driver.find_element(By.ID, "card_type").send_keys(card_type)
        self.driver.find_element(By.ID, "security_code").send_keys(security_code)
        self.driver.find_element(By.ID, "card_number").send_keys(card_number)
        self.driver.find_element(By.ID, "expiry_month").send_keys(expiration_month)
        self.driver.find_element(By.ID, "expiry_year").send_keys(expiration_year)

    def purchase_order_number_input(self, order_number):
        self.driver.find_element(*self.order_number).send_keys(order_number)

    def click_step_3_submit_button(self):
        self.driver.find_element(*self.step_3_submit_button)

    def click_step_3_previous_button(self):
        self.driver.find_element(*self.step_3_previous_button).click()

    def click_verify_credit_limit(self):
        self.driver.find_element(*self.verify_credit_limit).click()
        Alert(self.driver).accept()

    def is_page_opened(self):
        try:
            self.driver.find_element(*self.next_btn)
            return True
        except NoSuchElementException:
            return False, print("Orders page not opened")
