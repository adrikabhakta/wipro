from typing import List
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("SearchPage")


class SearchPage(BasePage):
    """
    Page Object representing the Product Search Results Page.
    URL: index.php?route=product/search
    """
    # Locators
    SEARCH_HEADER = (By.XPATH, "//h1[contains(text(), 'Search')]")
    PRODUCT_TITLES = (By.XPATH, "//div[@class='product-thumb']//h4/a")
    NO_PRODUCT_MESSAGE = (By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")
    SEARCH_CRITERIA_INPUT = (By.ID, "input-search")
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//a[@title='My Account']")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    RIGHT_COLUMN_LOGOUT = (By.XPATH, "//aside[@id='column-right']//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_search_results_titles(self) -> List[str]:
        """Returns list of product titles displayed in search results."""
        elements = self.find_elements(self.PRODUCT_TITLES)
        titles = [el.text.strip() for el in elements if el.text.strip()]
        logger.info(f"Found {len(titles)} products in search results: {titles}")
        return titles

    def is_product_present(self, product_name: str) -> bool:
        """Checks if a given product name is present among search results (case-insensitive)."""
        titles = self.get_search_results_titles()
        matched = any(product_name.lower() in title.lower() for title in titles)
        logger.info(f"Product '{product_name}' presence check: {matched}")
        return matched

    def get_no_product_message(self) -> str:
        """Returns message displayed when no products match criteria."""
        return self.get_element_text(self.NO_PRODUCT_MESSAGE)

    def is_no_product_message_displayed(self) -> bool:
        """Checks if 'no product found' message is visible."""
        return self.is_element_displayed(self.NO_PRODUCT_MESSAGE)

    def logout(self):
        """Logout user while on search page."""
        logger.info("Logging out from Search page")
        if self.is_element_displayed(self.RIGHT_COLUMN_LOGOUT):
            self.do_click(self.RIGHT_COLUMN_LOGOUT)
        else:
            self.do_click(self.MY_ACCOUNT_DROPDOWN)
            self.do_click(self.LOGOUT_LINK)
        from pages.logout_page import LogoutPage
        return LogoutPage(self.driver)
