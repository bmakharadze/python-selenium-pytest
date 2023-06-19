import time

import pytest

from Automation.Amazon.enums.Price import Price
from Automation.Amazon.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestAmazon:
    def test_add_book_to_the_cart(self, init_driver):
        home_page = HomePage(init_driver)

        time.sleep(2)
        home_page.change_address()
        products_page = home_page.click_today_deals_page()
        products_page.filter_by_books()
        product_page = products_page.click_product()
        product_page.click_add_to_cart()
        time.sleep(2)

    def test_search_product(self, init_driver):
        home_page = HomePage(init_driver)

        products_page = home_page.search_product()
        products_page.filter_by_price(Price.TO600)
        products_page.print_all_product_names()
