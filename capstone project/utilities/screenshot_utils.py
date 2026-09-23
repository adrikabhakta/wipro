from datetime import datetime
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("ScreenshotUtils")


class ScreenshotUtils:
    """
    Utility class for capturing screenshots on test failure or verification checkpoints.
    """
    @staticmethod
    def capture_screenshot(driver: WebDriver, test_name: str) -> str:
        """
        Captures screenshot and saves it as a PNG file in reports/screenshots/.
        Returns the absolute filepath string of the saved screenshot.
        """
        try:
            base_dir = Path(__file__).resolve().parent.parent
            screenshot_dir = base_dir / "reports" / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:19]
            safe_test_name = "".join([c if c.isalnum() or c in ("-", "_") else "_" for c in test_name])
            filename = f"{safe_test_name}_{timestamp}.png"
            file_path = screenshot_dir / filename

            driver.save_screenshot(str(file_path))
            logger.info(f"Screenshot successfully captured: {file_path}")
            return str(file_path)
        except Exception as e:
            logger.error(f"Failed to capture screenshot for test '{test_name}': {str(e)}")
            return ""

    @staticmethod
    def get_base64_screenshot(driver: WebDriver) -> str:
        """
        Returns the base64 encoded string of current screenshot for direct HTML embedding.
        """
        try:
            return driver.get_screenshot_as_base64()
        except Exception as e:
            logger.error(f"Failed to capture base64 screenshot: {str(e)}")
            return ""
