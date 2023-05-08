from Selenium.Openspan.enums.CreditCard import CreditCard
from Selenium.Openspan.enums.ExpirationMonth import ExpirationMonth
from Selenium.Openspan.enums.ExpirationYear import ExpirationYear
from Selenium.Openspan.enums.TestData import TestData
from enums.ProductList import ProductList
from enums.ProductType import ProductType
from pages.HomePage import HomePage
import pytest


@pytest.mark.usefixtures("init_driver")
class TestOpenspan:
    def test_add_products_to_cart_from_home_page(self, init_driver):
        # Create page objects
        home_page = HomePage(init_driver)

        # Select product from home page
        account_name = home_page.check_account_status()
        assert account_name == TestData.CHECK_ACCOUNT_NAME
        home_page.select_product_type(ProductType.BEVERAGES)
        home_page.select_product_list(ProductList.CHANG)
        product_page = home_page.click_view_products_button()
        assert product_page.is_product_page_opened()
        product_page.set_quantity(2)
        product_page.click_order_button()

    def test_add_products_to_cart_from_products_page(self, init_driver):
        home_page = HomePage(init_driver)

        products_page = home_page.click_products_page_button()
        products_page.click_beverages_button()
        product_page = products_page.click_product_button(ProductList.CHANG)
        assert product_page.is_product_page_opened()
        product_page.set_quantity(2)
        product_page.click_order_button()

    # Requires product to be in cart
    def test_order_products(self, init_driver):
        home_page = HomePage(init_driver)

        orders_page = home_page.click_order_menu_button()
        assert orders_page.is_page_opened()
        orders_page.click_next_button()
        orders_page.placeOrderStep2("john", "doe", "34223", "5111", "3234", "532555")
        orders_page.click_step_2_next_button()
        orders_page.placeOrderStep3(CreditCard.VISA, "4232", "342894239", ExpirationMonth.JULY,
                                    ExpirationYear.YEAR_2016)
        orders_page.click_step_3_submit_button()

    @pytest.mark.parametrize("order_details", [("john", "doe", "george", "1234", "4321", "yes", "3424")])
    def test_order_products_using_bill_me(self, init_driver, order_details):
        home_page = HomePage(init_driver)

        orders_page = home_page.click_order_menu_button()
        assert orders_page.is_page_opened()
        orders_page.click_next_button()
        orders_page.placeOrderStep2(*order_details[:6])
        orders_page.click_step_2_next_button()

        # Order using bill me
        orders_page.click_bill_me_button()
        orders_page.purchase_order_number_input(order_details[6])
        orders_page.click_verify_credit_limit()
        orders_page.click_step_3_submit_button()

