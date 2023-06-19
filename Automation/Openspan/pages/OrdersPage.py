from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from Automation.Openspan.base.BasePage import BasePage


class OrdersPage(BasePage):
    NEXT_BTN = (By.XPATH, '//*[@id="next1_button"]')
    STEP_2_NEXT_BUTTON = (By.XPATH, '//*[@id="next2_button"]')
    STEP_2_PREVIOUS_BUTTON = (By.XPATH, '//*[@name="previous"]')
    CREDIT_CARD = (By.XPATH, '//*[@id="credit_card"]')
    BILL_ME = (By.XPATH, '//*[@id="bill_me"]')
    ORDER_NUMBER = (By.XPATH, '//*[@id="purchase_order_number"]')
    STEP_3_SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit_button"]')
    STEP_3_PREVIOUS_BUTTON = (By.XPATH, '//*[@id="progressbar_container"]/fieldset[3]/input[1]')
    VERIFY_CREDIT_LIMIT = (By.ID, 'verify_credit_limit')

    def __init__(self, driver):
        super().__init__(driver)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BTN).click()

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
        self.driver.find_element(*self.STEP_2_NEXT_BUTTON).click()

    def click_step_2_previous_button(self):
        self.driver.find_element(*self.STEP_2_PREVIOUS_BUTTON).click()

    # STEP 3
    def click_credit_card_button(self):
        self.driver.find_element(*self.CREDIT_CARD).click()

    def click_bill_me_button(self):
        self.driver.find_element(*self.BILL_ME).click()

    def placeOrderStep3(self, card_type, security_code, card_number, expiration_month, expiration_year):
        self.driver.find_element(By.ID, "card_type").send_keys(card_type)
        self.driver.find_element(By.ID, "security_code").send_keys(security_code)
        self.driver.find_element(By.ID, "card_number").send_keys(card_number)
        self.driver.find_element(By.ID, "expiry_month").send_keys(expiration_month)
        self.driver.find_element(By.ID, "expiry_year").send_keys(expiration_year)

    def purchase_order_number_input(self, order_number):
        self.driver.find_element(*self.ORDER_NUMBER).send_keys(order_number)

    def click_step_3_submit_button(self):
        self.driver.find_element(*self.STEP_3_SUBMIT_BUTTON).click()

    def click_step_3_previous_button(self):
        self.driver.find_element(*self.STEP_2_PREVIOUS_BUTTON).click()

    def click_verify_credit_limit(self):
        self.driver.find_element(*self.VERIFY_CREDIT_LIMIT).click()
        Alert(self.driver).accept()

    def is_orders_page_opened(self):
        return super().is_page_opened(self.NEXT_BTN)
