import pytest
import allure
from config.config import BASE_URL
from data.excel_reader import get_excel_data
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.order_history_page import OrderHistoryPage

test_records = get_excel_data("test_data.xlsx")

@allure.epic("E-Commerce Automation")
@allure.feature("Checkout Flow")
@pytest.mark.parametrize("record", test_records)
def test_complete_checkout_process(driver, record):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)
    order_history_page = OrderHistoryPage(driver)

    with allure.step("1. Navigate to homepage"):
        home_page.navigate_to(BASE_URL)

    with allure.step("2. Authenticate user"):
        home_page.go_to_login()
        login_page.login(record["email"], record["password"])

    with allure.step(f"3. Search for product '{record['search_term']}' and add to cart"):
        home_page.search_for_product(record["search_term"])
        product_page.add_first_product_to_cart()
        product_page.proceed_to_checkout()

    with allure.step("4. Process checkout, shipping, and payment"):
        checkout_page.complete_standard_checkout()

    with allure.step("5. Validate order confirmation"):
        confirmation_msg = checkout_page.get_order_confirmation_text()
        assert "complete" in confirmation_msg.lower() or "placed" in confirmation_msg.lower(), \
            f"Expected completion message, received: {confirmation_msg}"
        order_reference = checkout_page.extract_order_reference()

    with allure.step("6. Verify order in order history"):
        order_history_page.go_to_order_history()
        assert order_history_page.is_order_present(order_reference), \
            f"Order reference {order_reference} not found in user history."