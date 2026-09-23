import unittest
import sys
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.config_reader import ConfigReader
from utilities.driver_factory import DriverFactory
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("UnittestBase")


class BaseTestCase(unittest.TestCase):
    """
    Base test case for Unittest test suites.
    Handles driver lifecycle, failure detection, and automatic failure screenshot capture.
    """
    driver: WebDriver

    def setUp(self):
        logger.info(f"--- Starting Unittest: {self._testMethodName} ---")
        browser = ConfigReader.get_browser()
        headless = ConfigReader.is_headless()
        self.driver = DriverFactory.get_driver(browser_name=browser, headless=headless)
        self.driver.get(ConfigReader.get_app_url())

    def tearDown(self):
        # Detect whether the test failed during execution
        # In Python standard unittest, _outcome contains result details
        test_failed = False
        outcome = getattr(self, "_outcome", None)
        if outcome:
            # Check errors or failures
            errors = getattr(outcome, "errors", [])
            for test_case, exc_info in errors:
                if exc_info:
                    test_failed = True
                    break

        if test_failed:
            logger.warning(f"Test '{self._testMethodName}' failed! Capturing failure screenshot.")
            ScreenshotUtils.capture_screenshot(self.driver, f"unittest_{self._testMethodName}")

        logger.info(f"--- Finished Unittest: {self._testMethodName} ---")
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                logger.error(f"Error terminating driver: {e}")
