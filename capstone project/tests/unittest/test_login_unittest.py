import unittest
from tests.unittest.base_test_case import BaseTestCase
from pages.home_page import HomePage
from pages.account_page import AccountPage
from utilities.config_reader import ConfigReader
from utilities.csv_utils import CSVUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestLoginUnittest")


class TestLoginUnittest(BaseTestCase):
    """
    Unittest test suite for Login workflows.
    """

    def test_valid_user_login(self):
        """Test successful login with registered credentials."""
        logger.info("Running Unittest: test_valid_user_login")
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()

        self.assertTrue(login_page.is_login_page_loaded(), "Login page failed to load.")

        valid_email = ConfigReader.get_credential("valid_email")
        valid_password = ConfigReader.get_credential("valid_password")

        account_page: AccountPage = login_page.login(valid_email, valid_password)

        self.assertTrue(account_page.is_my_account_page_displayed(), "Account dashboard was not displayed.")
        self.assertIn("Account", account_page.get_title(), "Page title did not contain 'Account'.")

        account_page.logout()

    def test_invalid_login_permutations_csv(self):
        """Test invalid login attempts driven by CSV test data."""
        logger.info("Running Unittest: test_invalid_login_permutations_csv")
        test_records = CSVUtils.get_csv_as_dicts("login_data.csv")

        for record in test_records:
            tc_id = record["test_case_id"]
            email = record["email"]
            password = record["password"]
            expected_outcome = record["expected_outcome"]
            expected_msg = record["expected_message"]

            with self.subTest(test_case=tc_id):
                logger.info(f"SubTest [{tc_id}] executing with email='{email}'")
                home_page = HomePage(self.driver)
                login_page = home_page.navigate_to_login_page()

                account_page = login_page.login(email, password)

                if expected_outcome == "success":
                    self.assertTrue(account_page.is_my_account_page_displayed())
                    account_page.logout()
                else:
                    self.assertTrue(login_page.is_warning_alert_displayed())
                    self.assertIn(expected_msg, login_page.get_warning_alert_text())


if __name__ == "__main__":
    unittest.main()
