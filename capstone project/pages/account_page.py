from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.logout_page import LogoutPage
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("AccountPage")


class AccountPage(BasePage):
    """
    Page Object representing the My Account Page (Dashboard).
    URL: index.php?route=account/account
    """
    # Locators
    MY_ACCOUNT_HEADER = (By.XPATH, "//div[@id='content']//h2[text()='My Account']")
    EDIT_ACCOUNT_LINK = (By.LINK_TEXT, "Edit your account information")
    LOGOUT_LINK = (By.XPATH, "//aside[@id='column-right']//a[text()='Logout']")
    ACCOUNT_BREADCRUMB = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Account']")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def __init__(self, driver):
        super().__init__(driver)

    def is_my_account_page_displayed(self) -> bool:
        """Verify whether My Account page header is visible."""
        return self.is_element_displayed(self.MY_ACCOUNT_HEADER)

    def is_edit_account_link_displayed(self) -> bool:
        """Verify edit account information option is present."""
        return self.is_element_displayed(self.EDIT_ACCOUNT_LINK)

    def search_for_product(self, product_name: str):
        """Perform product search directly from the account page header."""
        logger.info(f"AccountPage: Searching for product '{product_name}'")
        self.do_send_keys(self.SEARCH_INPUT, product_name)
        self.do_click(self.SEARCH_BUTTON)
        from pages.search_page import SearchPage
        return SearchPage(self.driver)

    def logout(self) -> LogoutPage:
        """Click logout link and navigate to Logout confirmation page."""
        logger.info("Logging out from Account dashboard")
        self.do_click(self.LOGOUT_LINK)
        return LogoutPage(self.driver)
