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


def test_openspan():
    # Initialize the Chrome driver and navigate to the website
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://training.openspan.com/login")
    driver.maximize_window()

    # Create page objects
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)
    product_page = ProductPage(driver)
    orders_page = OrdersPage(driver)

    # Perform login
    login_page.is_page_opened()
    login_page.login("testing", "testing123")
    login_page.click_login_button()

    # Select product from home page
    # home_page.is_page_opened()
    # home_page.select_product_type(ProductType.BEVERAGES)
    # home_page.select_product_list(ProductList.CHANG)
    # home_page.click_view_products_button()

    # Select product from products page
    products_page.is_page_opened()
    products_page.click_products_page_button()
    products_page.click_beverages_button()
    products_page.click_product_button(ProductList.CHANG)

    # Add product to the cart
    product_page.is_page_opened()
    product_page.set_quantity(2)
    product_page.click_order_button()

    # Order product
    orders_page.is_page_opened()
    orders_page.click_order_menu_button()
    orders_page.click_next_button()
    orders_page.placeOrderStep2("john", "doe", "george", "1234", "4321", "yes")
    orders_page.click_step_2_next_button()
    orders_page.placeOrderStep3(CreditCard.VISA, "4232", "342894239", ExpirationMonth.JULY, ExpirationYear.YEAR_2016)
    orders_page.click_bill_me_button()
    orders_page.purchase_order_number_input("3424")
    orders_page.click_verify_credit_limit()
    orders_page.click_step_3_submit_button()

