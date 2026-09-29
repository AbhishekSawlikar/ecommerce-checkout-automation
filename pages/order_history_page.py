from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderHistoryPage(BasePage):
    USER_ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, "a[title='Orders']")
    ORDER_ROWS = (By.CSS_SELECTOR, "#order-list tbody tr")

    def go_to_order_history(self):
        self.click(self.USER_ACCOUNT_LINK)
        self.click(self.ORDER_HISTORY_LINK)

    def is_order_present(self, order_ref):
        if not order_ref:
            # Fallback check if at least one recent order is recorded
            return len(self.driver.find_elements(*self.ORDER_ROWS)) > 0
        ref_locator = (By.XPATH, f"//a[contains(@class,'color-myaccount') and contains(text(),'{order_ref}')]")
        return len(self.driver.find_elements(*ref_locator)) > 0