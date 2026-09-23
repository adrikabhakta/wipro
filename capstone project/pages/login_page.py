from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("LoginPage")


class LoginPage(BasePage):
    """
    Page Object representing the Login Page.
    """
    # Locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_ALERT = (By.CSS_SELECTOR, ".alert-danger")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    RETURNING_CUSTOMER_HEADER = (By.XPATH, "//h2[text()='Returning Customer']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email: str) -> None:
        """Enter email address into email field."""
        self.do_send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password: str) -> None:
        """Enter password into password field."""
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        """Click the Login button."""
        self.do_click(self.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        """Perform complete login action with given credentials."""
        logger.info(f"Attempting login with email: {email}")
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        from pages.account_page import AccountPage
        return AccountPage(self.driver)

    def get_warning_alert_text(self) -> str:
        """Retrieve error alert message text."""
        return self.get_element_text(self.WARNING_ALERT)

    def is_warning_alert_displayed(self) -> bool:
        """Check if error alert banner is displayed."""
        return self.is_element_displayed(self.WARNING_ALERT)

    def is_login_page_loaded(self) -> bool:
        """Verify presence of Returning Customer header."""
        return self.is_element_displayed(self.RETURNING_CUSTOMER_HEADER)
