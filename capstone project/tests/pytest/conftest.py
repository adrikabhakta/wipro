import pytest
from pytest_html import extras
from utilities.config_reader import ConfigReader
from utilities.driver_factory import DriverFactory
from utilities.screenshot_utils import ScreenshotUtils
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("PyTestConftest")


def pytest_addoption(parser):
    """Register custom command-line options."""
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests on: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store",
        default=None,
        help="Run browser in headless mode: true or false"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Function-scoped fixture to initialize and tear down WebDriver.
    Loads the target application URL configured in config.ini.
    """
    cli_browser = request.config.getoption("--browser")
    cli_headless = request.config.getoption("--headless")

    browser = cli_browser if cli_browser else ConfigReader.get_browser()
    if cli_headless is not None:
        headless = str(cli_headless).lower() in ("true", "1", "yes")
    else:
        headless = ConfigReader.is_headless()

    logger.info(f"Starting test session with browser={browser}, headless={headless}")
    web_driver = DriverFactory.get_driver(browser_name=browser, headless=headless)

    # Attach driver to test node so hook can access it on failure
    request.node.driver = web_driver

    app_url = ConfigReader.get_app_url()
    logger.info(f"Navigating to application URL: {app_url}")
    web_driver.get(app_url)

    yield web_driver

    logger.info("Tearing down WebDriver session")
    try:
        web_driver.quit()
    except Exception as e:
        logger.warning(f"Error while quitting driver: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure and embed it into pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Retrieve driver instance from item
        driver_instance = getattr(item, "driver", None)
        if not driver_instance and "driver" in item.funcargs:
            driver_instance = item.funcargs["driver"]

        if driver_instance:
            screenshot_path = ScreenshotUtils.capture_screenshot(driver_instance, item.name)
            base64_img = ScreenshotUtils.get_base64_screenshot(driver_instance)

            # pytest-html 4.x uses report.extras list
            report_extras = getattr(report, "extras", None)
            if report_extras is None:
                report_extras = getattr(report, "extra", [])
                setattr(report, "extra", report_extras)
            else:
                setattr(report, "extras", report_extras)

            if base64_img:
                html_content = (
                    f'<div style="margin: 10px 0;">'
                    f'<h4 style="color: #d9534f;">Failure Screenshot:</h4>'
                    f'<img src="data:image/png;base64,{base64_img}" '
                    f'style="max-width: 600px; max-height: 400px; border: 2px solid #d9534f; border-radius: 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);" />'
                    f'</div>'
                )
                report_extras.append(extras.html(html_content))
            elif screenshot_path:
                report_extras.append(extras.image(screenshot_path))


def pytest_html_report_title(report):
    """Custom title for the HTML report."""
    report.title = "Selenium Automation Test Execution Report - TutorialsNinja"


def pytest_configure(config):
    """Add custom environment metadata to the report."""
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Selenium Python Capstone Automation"
        config._metadata["Application"] = "TutorialsNinja E-Commerce"
        config._metadata["Architecture"] = "Page Object Model (POM) + PyTest + Unittest"
        config._metadata["Base URL"] = ConfigReader.get_app_url()
        config._metadata["Execution Mode"] = "Headless" if ConfigReader.is_headless() else "Headed"
