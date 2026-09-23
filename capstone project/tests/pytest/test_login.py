import pytest
from pages.home_page import HomePage
from pages.account_page import AccountPage
from utilities.config_reader import ConfigReader
from utilities.csv_utils import CSVUtils
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestLoginPyTest")


@pytest.mark.login
class TestLogin:
    """
    Test suite for Login functionality using PyTest, Page Object Model,
    and CSV Data-Driven Testing.
    """

    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """
        Verify that a registered user can log in successfully with valid credentials.
        """
        logger.info("Executing test_valid_login")
        home_page = HomePage(driver)
        login_page = home_page.navigate_to_login_page()
        ScreenshotUtils.capture_screenshot(driver, "step_01_login_page")

        assert login_page.is_login_page_loaded(), "Login page header 'Returning Customer' was not displayed"

        valid_email = ConfigReader.get_credential("valid_email")
        valid_password = ConfigReader.get_credential("valid_password")

        account_page: AccountPage = login_page.login(valid_email, valid_password)
        ScreenshotUtils.capture_screenshot(driver, "step_02_account_dashboard")

        assert account_page.is_my_account_page_displayed(), "My Account page was not displayed after valid login"
        assert "Account" in account_page.get_title(), f"Page title does not contain 'Account': {account_page.get_title()}"

        # Clean up session
        account_page.logout()
        logger.info("test_valid_login passed successfully")

    @pytest.mark.regression
    @pytest.mark.data_driven
    @pytest.mark.parametrize(
        "test_case_id,email,password,expected_outcome,expected_message",
        CSVUtils.get_csv_as_tuples(
            "login_data.csv",
            ["test_case_id", "email", "password", "expected_outcome", "expected_message"]
        )
    )
    def test_login_data_driven(self, driver, test_case_id, email, password, expected_outcome, expected_message):
        """
        Data-driven test verifying various login credential permutations loaded from CSV.
        """
        logger.info(f"Executing {test_case_id} | Outcome expected: {expected_outcome}")
        home_page = HomePage(driver)
        login_page = home_page.navigate_to_login_page()

        account_page = login_page.login(email, password)

        if expected_outcome == "success":
            assert account_page.is_my_account_page_displayed(), f"[{test_case_id}] Expected successful login, but account page not found."
            account_page.logout()
        else:
            assert login_page.is_warning_alert_displayed(), f"[{test_case_id}] Warning alert was not displayed."
            alert_text = login_page.get_warning_alert_text()
            assert expected_message in alert_text, f"[{test_case_id}] Expected message '{expected_message}' not found in alert text '{alert_text}'"

        logger.info(f"{test_case_id} completed successfully")
