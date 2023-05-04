import pytest
from selenium import webdriver
import time
import logging
from enums.ProductList import ProductList
from enums.ProductType import ProductType
from enums.CreditCard import CreditCard
from enums.ExpirationMonth import ExpirationMonth
from enums.ExpirationYear import ExpirationYear
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

# # PYTEST

# Configure the logging module
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def driver(request):
    logging.info("Setting up driver...")
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://training.openspan.com/login")

    # For every test it is needed to be logged in to the website
    login_page = LoginPage(driver)
    assert login_page.is_login_page_opened(), "Login page is not opened."
    login_page.login("testing", "testing123")
    login_page.click_login_button()

    yield driver
    driver.quit()


@pytest.mark.parametrize("driver", [("chrome")], indirect=True)
def test_add_products_to_cart_from_home_page(driver):
    # Create page objects
    home_page = HomePage(driver)

    # Select product from home page
    home_page.select_product_type(ProductType.BEVERAGES)
    home_page.select_product_list(ProductList.CHANG)
    product_page = home_page.click_view_products_button()
    assert product_page.is_product_page_opened(), "Product page is not opened."
    product_page.set_quantity(2)
    product_page.click_order_button()


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_add_products_to_cart_from_products_page(driver):
    home_page = HomePage(driver)

    products_page = home_page.click_products_page_button()
    products_page.click_beverages_button()
    product_page = products_page.click_product_button(ProductList.CHANG)
    assert product_page.is_product_page_opened(), "Product page is not opened."
    product_page.set_quantity(2)
    product_page.click_order_button()


# Requires product to be in cart
@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_order_products(driver, first_name, last_name, middle_name, credit_card_number, security_code, bill_me):
    home_page = HomePage(driver)

    orders_page = home_page.click_order_menu_button()
    assert orders_page.is_page_opened(), "Orders page is not opened."
    orders_page.click_next_button()
    orders_page.placeOrderStep2(first_name, last_name, middle_name, credit_card_number, security_code, bill_me)
    orders_page.click_step_2_next_button()
    orders_page.placeOrderStep3(CreditCard.VISA, "4232", "342894239", ExpirationMonth.JULY, ExpirationYear.YEAR_2016)
    orders_page.click_step_3_submit_button()


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
@pytest.mark.parametrize("order_details", [("john", "doe", "george", "1234", "4321", "yes", "3424")])
def test_order_products_using_bill_me(driver, order_details):
    home_page = HomePage(driver)

    orders_page = home_page.click_order_menu_button()
    assert orders_page.is_page_opened(), "Orders page is not opened."
    orders_page.click_next_button()
    orders_page.placeOrderStep2(*order_details[:6])
    orders_page.click_step_2_next_button()

    # Order using bill me
    orders_page.click_bill_me_button()
    orders_page.purchase_order_number_input(order_details[6])
    orders_page.click_verify_credit_limit()
    orders_page.click_step_3_submit_button()

