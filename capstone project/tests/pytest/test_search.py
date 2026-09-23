import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.csv_utils import CSVUtils
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("TestSearchPyTest")


@pytest.mark.search
class TestSearch:
    """
    Test suite for Product Search functionality using PyTest, Page Object Model,
    and CSV Data-Driven Testing.
    """

    @pytest.mark.smoke
    def test_search_existing_product(self, driver):
        """
        Verify that searching for an existing product returns matching results.
        """
        product = "MacBook"
        logger.info(f"Executing test_search_existing_product for '{product}'")
        home_page = HomePage(driver)
        search_page: SearchPage = home_page.search_for_product(product)
        ScreenshotUtils.capture_screenshot(driver, "step_03_search_macbook")

        titles = search_page.get_search_results_titles()
        assert len(titles) > 0, "Expected search results, but found none."
        assert search_page.is_product_present(product), f"Expected product '{product}' not found in results: {titles}"
        logger.info("test_search_existing_product passed successfully")

    @pytest.mark.smoke
    def test_search_non_existent_product(self, driver):
        """
        Verify that searching for a non-existent product displays an informative message.
        """
        invalid_item = "XYZNonExistentDevice999"
        logger.info(f"Executing test_search_non_existent_product for '{invalid_item}'")
        home_page = HomePage(driver)
        search_page: SearchPage = home_page.search_for_product(invalid_item)
        ScreenshotUtils.capture_screenshot(driver, "step_04_search_not_found")

        assert search_page.is_no_product_message_displayed(), "No-product message was not displayed"
        msg = search_page.get_no_product_message()
        assert "There is no product that matches the search criteria." in msg, f"Unexpected message text: {msg}"
        logger.info("test_search_non_existent_product passed successfully")

    @pytest.mark.regression
    @pytest.mark.data_driven
    @pytest.mark.parametrize(
        "search_term,expected_status,expected_product_or_message",
        CSVUtils.get_csv_as_tuples(
            "search_data.csv",
            ["search_term", "expected_status", "expected_product_or_message"]
        )
    )
    def test_search_data_driven(self, driver, search_term, expected_status, expected_product_or_message):
        """
        Data-driven test verifying multiple search queries loaded from CSV dataset.
        """
        logger.info(f"Executing data-driven search for '{search_term}', expecting status: {expected_status}")
        home_page = HomePage(driver)
        search_page: SearchPage = home_page.search_for_product(search_term)

        if expected_status == "found":
            assert search_page.is_product_present(expected_product_or_message), (
                f"Expected product '{expected_product_or_message}' not found for search '{search_term}'."
            )
        else:
            assert search_page.is_no_product_message_displayed(), (
                f"Expected no-product message for search '{search_term}', but it was not displayed."
            )
            msg = search_page.get_no_product_message()
            assert expected_product_or_message in msg, (
                f"Expected '{expected_product_or_message}' in message, got '{msg}'"
            )

        logger.info(f"Data-driven search test for '{search_term}' passed")
