from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGN_IN_LINK = (By.CSS_SELECTOR, "a.login")
    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")

    def navigate_to(self, url):
        self.driver.get(url)

    def go_to_login(self):
        self.click(self.SIGN_IN_LINK)

    def search_for_product(self, product_name):
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)