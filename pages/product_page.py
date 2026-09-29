from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, "ul.product_list li.ajax_block_product")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "a.ajax_add_to_cart_button")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def add_first_product_to_cart(self):
        self.scroll_into_view(self.PRODUCT_CONTAINER)
        self.hover(self.PRODUCT_CONTAINER)
        self.click(self.ADD_TO_CART_BTN)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)