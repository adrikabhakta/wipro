from typing import List, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utilities.config_reader import ConfigReader
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("BasePage")


class BasePage:
    """
    BasePage encapsulates common Selenium WebDriver interactions,
    providing standardized explicit wait mechanisms and robust logging.
    """

    def __init__(self, driver: WebDriver, timeout: int = None):
        self.driver = driver
        self.timeout = timeout if timeout is not None else ConfigReader.get_explicit_wait()
        self.wait = WebDriverWait(self.driver, self.timeout)

    def do_click(self, locator: Tuple[str, str]) -> None:
        """Wait for element to be clickable and perform click."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            logger.info(f"Clicking element: {locator}")
            element.click()
        except TimeoutException:
            logger.error(f"Timeout waiting for element to be clickable: {locator}")
            raise

    def do_send_keys(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """Wait for element visibility, optionally clear, and enter text."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear_first:
                element.clear()
            logger.info(f"Entering text into element {locator}")
            element.send_keys(text)
        except TimeoutException:
            logger.error(f"Timeout waiting for element visibility: {locator}")
            raise

    def get_element_text(self, locator: Tuple[str, str]) -> str:
        """Wait for element visibility and return its text content."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text.strip()
            logger.info(f"Retrieved text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            logger.error(f"Timeout waiting for element text: {locator}")
            raise

    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        """Check if element is visible on page without raising timeout error."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Find and return list of elements matching locator."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Scroll element into view using JavaScript."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def get_title(self) -> str:
        """Return page title."""
        title = self.driver.title
        logger.info(f"Current page title: '{title}'")
        return title

    def get_current_url(self) -> str:
        """Return current browser URL."""
        return self.driver.current_url
