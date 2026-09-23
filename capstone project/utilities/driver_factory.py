from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.config_reader import ConfigReader
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("DriverFactory")


class DriverFactory:
    """
    Factory to initialize and configure Selenium WebDrivers.
    Supports Chrome, Firefox, and Edge with optional headless mode.
    """

    @staticmethod
    def get_driver(browser_name: str = None, headless: bool = None) -> WebDriver:
        if browser_name is None:
            browser_name = ConfigReader.get_browser()
        if headless is None:
            headless = ConfigReader.is_headless()

        browser_name = browser_name.lower().strip()
        logger.info(f"Initializing WebDriver for browser='{browser_name}', headless={headless}")

        driver: WebDriver

        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-notifications")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)

        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)

        else:
            logger.warning(f"Browser '{browser_name}' not explicitly configured, falling back to Chrome.")
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        # Maximize window in headed mode for real visibility
        if not headless:
            try:
                driver.maximize_window()
            except Exception:
                pass

        # Apply timeouts
        implicit_wait = ConfigReader.get_implicit_wait()
        driver.implicitly_wait(implicit_wait)
        driver.set_page_load_timeout(30)
        logger.info(f"WebDriver successfully initialized with implicit_wait={implicit_wait}s")

        return driver
