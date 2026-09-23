import unittest
from tests.unittest.base_test_case import BaseTestCase
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.csv_utils import CSVUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestSearchUnittest")


class TestSearchUnittest(BaseTestCase):
    """
    Unittest test suite for Product Search workflows.
    """

    def test_search_for_valid_product(self):
        """Test searching for an existing product (MacBook)."""
        logger.info("Running Unittest: test_search_for_valid_product")
        home_page = HomePage(self.driver)
        search_page: SearchPage = home_page.search_for_product("MacBook")

        self.assertTrue(search_page.is_product_present("MacBook"), "Product 'MacBook' not found in results.")
        self.assertGreater(len(search_page.get_search_results_titles()), 0, "No products displayed in search results.")

    def test_search_for_non_existent_product(self):
        """Test searching for a non-existent item."""
        logger.info("Running Unittest: test_search_for_non_existent_product")
        home_page = HomePage(self.driver)
        search_page: SearchPage = home_page.search_for_product("NonExistentItem9999")

        self.assertTrue(search_page.is_no_product_message_displayed(), "No-product message not displayed.")
        self.assertIn("There is no product that matches the search criteria.", search_page.get_no_product_message())

    def test_search_data_driven_csv(self):
        """Test search queries driven by search_data.csv."""
        logger.info("Running Unittest: test_search_data_driven_csv")
        records = CSVUtils.get_csv_as_dicts("search_data.csv")

        for record in records:
            term = record["search_term"]
            status = record["expected_status"]
            expected = record["expected_product_or_message"]

            with self.subTest(search_term=term, expected_status=status):
                logger.info(f"SubTest search term: '{term}'")
                home_page = HomePage(self.driver)
                search_page: SearchPage = home_page.search_for_product(term)

                if status == "found":
                    self.assertTrue(
                        search_page.is_product_present(expected),
                        f"Expected product '{expected}' not found for term '{term}'."
                    )
                else:
                    self.assertTrue(search_page.is_no_product_message_displayed())
                    self.assertIn(expected, search_page.get_no_product_message())


if __name__ == "__main__":
    unittest.main()
