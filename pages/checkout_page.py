import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Summary
    PROCEED_SUMMARY_BTN = (By.CSS_SELECTOR, "p.cart_navigation a[title='Proceed to checkout']")
    # Address
    PROCEED_ADDRESS_BTN = (By.NAME, "processAddress")
    # Shipping
    TERMS_CHECKBOX = (By.ID, "cgv")
    PROCEED_SHIPPING_BTN = (By.NAME, "processCarrier")
    # Payment
    PAY_BY_BANK_WIRE = (By.CSS_SELECTOR, "a.bankwire")
    CONFIRM_ORDER_BTN = (By.CSS_SELECTOR, "#cart_navigation button[type='submit']")
    ORDER_CONFIRMATION_BOX = (By.CSS_SELECTOR, "div.box")
    ORDER_SUCCESS_TEXT = (By.CSS_SELECTOR, "p.alert-success, p.cheque-indent strong")

    def complete_standard_checkout(self):
        # 1. Summary Step
        self.click(self.PROCEED_SUMMARY_BTN)
        # 2. Address Step (Default address assumed for existing user)
        self.click(self.PROCEED_ADDRESS_BTN)
        # 3. Shipping Step (Accept Terms)
        self.click(self.TERMS_CHECKBOX)
        self.click(self.PROCEED_SHIPPING_BTN)
        # 4. Payment Step
        self.click(self.PAY_BY_BANK_WIRE)
        self.click(self.CONFIRM_ORDER_BTN)

    def get_order_confirmation_text(self):
        return self.get_text(self.ORDER_SUCCESS_TEXT)

    def extract_order_reference(self):
        box_text = self.get_text(self.ORDER_CONFIRMATION_BOX)
        # Typical pattern: "reference [A-Z]{9}" or "order reference: XXXXX"
        match = re.search(r"reference\s+([A-Z0-9]+)", box_text)
        return match.group(1) if match else None