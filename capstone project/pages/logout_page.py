from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("LogoutPage")


class LogoutPage(BasePage):
    """
    Page Object representing the Account Logout confirmation page.
    URL: index.php?route=account/logout
    """
    LOGOUT_HEADER = (By.XPATH, "//div[@id='content']//h1[text()='Account Logout']")
    LOGOUT_MESSAGE = (By.XPATH, "//div[@id='content']//p[contains(text(), 'You have been logged off your account')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-primary') and text()='Continue']")
    ACCOUNT_BREADCRUMB_LOGOUT = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_logout_header_displayed(self) -> bool:
        """Verify whether Account Logout header is displayed."""
        return self.is_element_displayed(self.LOGOUT_HEADER)

    def is_logout_message_displayed(self) -> bool:
        """Verify whether logout success text is displayed."""
        return self.is_element_displayed(self.LOGOUT_MESSAGE)

    def is_continue_button_displayed(self) -> bool:
        """Verify presence of Continue button."""
        return self.is_element_displayed(self.CONTINUE_BUTTON)

    def click_continue(self):
        """Click Continue button to return to home page."""
        logger.info("Clicking Continue on Logout confirmation page")
        self.do_click(self.CONTINUE_BUTTON)
        from pages.home_page import HomePage
        return HomePage(self.driver)
