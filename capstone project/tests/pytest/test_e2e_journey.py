import pytest
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.search_page import SearchPage
from pages.logout_page import LogoutPage
from utilities.config_reader import ConfigReader
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestE2EJourneyPyTest")


@pytest.mark.e2e
class TestE2EJourney:
    """
    Capstone End-to-End User Journey Test Suite.
    Scenario:
        1. Login with valid credentials
        2. Verify login (Dashboard / My Account)
        3. Product Search
        4. Verify search results
        5. Logout and verify logout confirmation
    """

    def test_complete_user_journey(self, driver):
        """
        Executes and asserts full flow:
        Login -> verify login -> Product Search -> verify results -> Logout
        """
        logger.info(">>> Starting Capstone E2E Flow: Login -> Verify -> Search -> Verify -> Logout")

        # Step 1: Navigate to Login Page
        home_page = HomePage(driver)
        login_page = home_page.navigate_to_login_page()
        assert login_page.is_login_page_loaded(), "Login page failed to load properly."
        ScreenshotUtils.capture_screenshot(driver, "e2e_01_login_page")

        # Step 2: Login with valid credentials
        valid_email = ConfigReader.get_credential("valid_email")
        valid_password = ConfigReader.get_credential("valid_password")
        logger.info(f"Logging in with credentials: {valid_email}")

        account_page: AccountPage = login_page.login(valid_email, valid_password)

        # Step 3: Verify login success
        assert account_page.is_my_account_page_displayed(), "Verification Failed: 'My Account' header is not displayed."
        assert "Account" in account_page.get_title(), f"Verification Failed: Title does not contain 'Account'. Actual: {account_page.get_title()}"
        ScreenshotUtils.capture_screenshot(driver, "e2e_02_login_verified")
        logger.info("[SUCCESS] Step 1 & 2 Verified: User logged in successfully.")

        # Step 4: Product Search
        search_query = "MacBook"
        logger.info(f"Initiating product search for: '{search_query}'")
        search_page: SearchPage = account_page.search_for_product(search_query)

        # Step 5: Verify search results
        results = search_page.get_search_results_titles()
        logger.info(f"Search results returned: {results}")
        assert len(results) > 0, f"Verification Failed: No search results returned for query '{search_query}'."
        assert search_page.is_product_present(search_query), f"Verification Failed: '{search_query}' not found in search results."
        ScreenshotUtils.capture_screenshot(driver, "e2e_03_search_results_verified")
        logger.info("[SUCCESS] Step 3 & 4 Verified: Product search returned expected results.")

        # Step 6: Logout
        logger.info("Initiating user logout")
        logout_page: LogoutPage = search_page.logout()

        # Step 7: Verify logout confirmation
        assert logout_page.is_logout_header_displayed(), "Verification Failed: 'Account Logout' header was not displayed."
        assert logout_page.is_logout_message_displayed(), "Verification Failed: Logout confirmation message was not displayed."
        assert logout_page.is_continue_button_displayed(), "Verification Failed: 'Continue' button not present on logout page."
        ScreenshotUtils.capture_screenshot(driver, "e2e_04_logout_verified")
        logger.info("[SUCCESS] Step 5 Verified: User successfully logged out.")

        logger.info(">>> Capstone E2E Flow completed with 100% success!")
