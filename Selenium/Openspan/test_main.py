import pytest
from selenium import webdriver
import time
from enums.ProductList import ProductList
from enums.ProductType import ProductType
from enums.CreditCard import CreditCard
from enums.ExpirationMonth import ExpirationMonth
from enums.ExpirationYear import ExpirationYear
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.ProductPage import ProductPage
from pages.HomePage import HomePage
from pages.OrdersPage import OrdersPage


# # PYTEST


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://training.openspan.com/login")

    # For every test it is needed to be logged in to the website
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "Login page is not opened."
    login_page.login("testing", "testing123")
    login_page.click_login_button()

    yield driver
    driver.quit()


def test_add_products_to_cart_from_home_page(driver):
    # Create page objects
    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    # Select product from home page
    assert home_page.is_page_opened(), "Home page is not opened."
    home_page.select_product_type(ProductType.BEVERAGES)
    home_page.select_product_list(ProductList.CHANG)
    home_page.click_view_products_button()

    # Add product to the cart
    assert product_page.is_page_opened(), "Product page is not opened."
    product_page.set_quantity(2)
    product_page.click_order_button()


def test_add_products_to_cart_from_products_page(driver):
    products_page = ProductsPage(driver)
    product_page = ProductPage(driver)

    products_page.click_products_page_button()
    assert products_page.is_page_opened(), "Products page is not opened."
    products_page.click_beverages_button()
    products_page.click_product_button(ProductList.CHANG)

    assert product_page.is_page_opened(), "Product page is not opened."
    product_page.set_quantity(2)
    product_page.click_order_button()


# Requires product to be in cart
def test_order_products(driver):
    orders_page = OrdersPage(driver)

    # Order product
    orders_page.click_order_menu_button()
    assert orders_page.is_page_opened(), "Orders page is not opened."
    orders_page.click_next_button()
    orders_page.placeOrderStep2("john", "doe", "george", "1234", "4321", "yes")
    orders_page.click_step_2_next_button()
    orders_page.placeOrderStep3(CreditCard.VISA, "4232", "342894239", ExpirationMonth.JULY, ExpirationYear.YEAR_2016)
    orders_page.click_step_3_submit_button()


def test_order_products_using_bill_me(driver):
    orders_page = OrdersPage(driver)

    # Order product
    orders_page.click_order_menu_button()
    assert orders_page.is_page_opened(), "Orders page is not opened."
    orders_page.click_next_button()
    orders_page.placeOrderStep2("john", "doe", "george", "1234", "4321", "yes")
    orders_page.click_step_2_next_button()

    # Order using bill me
    orders_page.click_bill_me_button()
    orders_page.purchase_order_number_input("3424")
    orders_page.click_verify_credit_limit()
    orders_page.click_step_3_submit_button()
