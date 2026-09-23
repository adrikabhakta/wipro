from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("HomePage")


class HomePage(BasePage):
    """
    Page Object representing the TutorialsNinja Home Page.
    """
    # Locators
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//a[@title='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    LOGO = (By.CSS_SELECTOR, "#logo a")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_page(self) -> LoginPage:
        """Click My Account dropdown and select Login link."""
        logger.info("Navigating to Login page from Home page")
        self.do_click(self.MY_ACCOUNT_DROPDOWN)
        self.do_click(self.LOGIN_LINK)
        return LoginPage(self.driver)

    def search_for_product(self, product_name: str) -> SearchPage:
        """Enter product name in search box and click search button."""
        logger.info(f"Searching for product: '{product_name}'")
        self.do_send_keys(self.SEARCH_INPUT, product_name)
        self.do_click(self.SEARCH_BUTTON)
        return SearchPage(self.driver)

    def is_logo_displayed(self) -> bool:
        """Verify presence of homepage logo."""
        return self.is_element_displayed(self.LOGO)
