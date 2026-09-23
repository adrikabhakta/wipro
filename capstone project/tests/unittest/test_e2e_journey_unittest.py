import unittest
from tests.unittest.base_test_case import BaseTestCase
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.search_page import SearchPage
from pages.logout_page import LogoutPage
from utilities.config_reader import ConfigReader
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestE2EJourneyUnittest")


class TestE2EJourneyUnittest(BaseTestCase):
    """
    Capstone Unittest End-to-End User Journey Test Suite.
    Scenario:
        1. Login with valid credentials
        2. Verify login (Dashboard / My Account)
        3. Product Search
        4. Verify search results
        5. Logout and verify logout confirmation
    """

    def test_e2e_login_search_logout(self):
        """
        Executes and verifies:
        Login -> verify login -> Product Search -> verify results -> Logout
        """
        logger.info("Executing Unittest E2E: Login -> Verify -> Search -> Verify -> Logout")

        # Step 1: Navigate to Login Page
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        self.assertTrue(login_page.is_login_page_loaded(), "Login page failed to load.")
        ScreenshotUtils.capture_screenshot(self.driver, "unittest_e2e_01_login_page")

        # Step 2: Login with valid credentials
        valid_email = ConfigReader.get_credential("valid_email")
        valid_password = ConfigReader.get_credential("valid_password")
        account_page: AccountPage = login_page.login(valid_email, valid_password)

        # Step 3: Verify login
        self.assertTrue(account_page.is_my_account_page_displayed(), "Account dashboard was not displayed after login.")
        self.assertIn("Account", account_page.get_title(), "Page title did not contain 'Account'.")
        ScreenshotUtils.capture_screenshot(self.driver, "unittest_e2e_02_login_verified")

        # Step 4: Product Search
        search_query = "MacBook"
        search_page: SearchPage = account_page.search_for_product(search_query)

        # Step 5: Verify search results
        titles = search_page.get_search_results_titles()
        self.assertGreater(len(titles), 0, f"No search results returned for query '{search_query}'.")
        self.assertTrue(search_page.is_product_present(search_query), f"'{search_query}' not found in search results.")
        ScreenshotUtils.capture_screenshot(self.driver, "unittest_e2e_03_search_verified")

        # Step 6: Logout
        logout_page: LogoutPage = search_page.logout()

        # Step 7: Verify logout
        self.assertTrue(logout_page.is_logout_header_displayed(), "Account Logout header was not displayed.")
        self.assertTrue(logout_page.is_logout_message_displayed(), "Logout confirmation message not displayed.")
        self.assertTrue(logout_page.is_continue_button_displayed(), "Continue button was not displayed on logout page.")
        ScreenshotUtils.capture_screenshot(self.driver, "unittest_e2e_04_logout_verified")

        logger.info("Unittest E2E user journey completed successfully!")


if __name__ == "__main__":
    unittest.main()
