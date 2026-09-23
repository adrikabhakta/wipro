# Selenium Python Automation Framework (Unittest + PyTest + POM)

A robust, enterprise-ready test automation framework engineered in Python using **Selenium WebDriver 4**, implementing the **Page Object Model (POM)** architectural design pattern, supporting dual test runners (**PyTest** & **Unittest**), dynamic configuration management, CSV data-driven testing, automatic failure screenshots, and self-contained HTML reporting.

---

## Architecture Overview

```
selenium_python_framework/
├── config/
│   ├── config.ini                  # Central configuration (URLs, browser, timeouts, headless)
│   └── __init__.py
├── utilities/
│   ├── __init__.py
│   ├── config_reader.py            # Parser for config.ini with typed getters
│   ├── driver_factory.py           # Cross-browser WebDriver factory (Chrome, Firefox, Edge)
│   ├── logger.py                   # Custom dual console/file logger
│   ├── csv_utils.py                # CSV data parsing for data-driven testing
│   └── screenshot_utils.py         # Failure screenshot and base64 encoding utilities
├── test_data/
│   ├── login_data.csv              # Credential permutations (valid, invalid, empty)
│   └── search_data.csv             # Product search queries and expected results
├── pages/
│   ├── __init__.py
│   ├── base_page.py                # Core wrapper (explicit waits, clicks, inputs, scrolls)
│   ├── home_page.py                # Header, navigation, search bar, login navigation
│   ├── login_page.py               # Credentials entry, submission, alert verification
│   ├── search_page.py              # Results grid, product matching, no-product messages
│   └── account_page.py             # Dashboard verification and logout handling
├── tests/
│   ├── pytest/
│   │   ├── conftest.py             # PyTest fixtures, CLI options, HTML report screenshot hooks
│   │   ├── test_login.py           # Smoke and CSV data-driven login tests
│   │   └── test_search.py          # Product search and negative query tests
│   └── unittest/
│       ├── base_test_case.py       # Base unittest class with failure screenshot capture
│       ├── test_login_unittest.py  # Unittest login test suite
│       └── test_search_unittest.py # Unittest product search test suite
├── reports/
│   ├── report.html                 # Self-contained HTML execution report
│   ├── screenshots/                # Timestamped failure screenshots (.png)
│   └── logs/
│       └── automation.log          # Detailed timestamped execution logs
├── run_tests.py                    # Unified CLI test runner
├── pytest.ini                      # PyTest configurations, markers, and defaults
├── requirements.txt                # Python dependencies
└── README.md                       # Comprehensive framework documentation
```

---

## Key Features & Design Principles

### 1. Page Object Model (POM)
- **Separation of Concerns**: Web page locators and actions are strictly encapsulated in page classes (`BasePage`, `HomePage`, `LoginPage`, `SearchPage`, `AccountPage`).
- **Explicit Synchronization**: All interactions use `WebDriverWait` with `expected_conditions` (clickable, visible, presence) instead of arbitrary sleep statements.
- **Maintainability**: When UI locators change, only the corresponding Page Object class needs modification.

### 2. Dual Runner Support (PyTest & Unittest)
- **PyTest Suite**: Leverages fixtures (`conftest.py`), `@pytest.mark.parametrize` for data-driven testing, custom CLI flags, and report hooks.
- **Unittest Suite**: Demonstrates classic enterprise `unittest.TestCase` inheritance, `setUp()`, `tearDown()`, `subTest` assertions, and automated failure detection.

### 3. Data-Driven Testing (CSV)
- Test cases dynamically consume external CSV data (`test_data/login_data.csv` and `test_data/search_data.csv`).
- Each dataset row executes as an independent test iteration with granular assertion reporting.

### 4. Automatic Failure Screenshots
- When a test assertion or unexpected condition fails, a high-resolution screenshot is automatically captured.
- Screenshots are saved with timestamped filenames in `reports/screenshots/` and embedded directly as Base64/PNG into the PyTest HTML report.

### 5. Centralized Configuration Management
- Application URL, default browser, headless flag, and timeout values are managed in `config/config.ini`.
- Can be dynamically overridden at runtime via CLI parameters (`--browser`, `--headless`).

### 6. Logging & Reporting
- Detailed logging with level, filename, line number, and timestamps to both console and `reports/logs/automation.log`.
- Rich, standalone HTML report generated at `reports/report.html` with environment metadata, duration, pass/fail status, and embedded screenshots.

---

## Installation & Setup

1. **Clone or Navigate to the Workspace Directory**:
   ```bash
   cd /Users/adrika/.gemini/antigravity-ide/scratch/selenium_python_framework
   ```

2. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Execution Guide

### Option 1: Using the Unified CLI Runner (`run_tests.py`)

Run all PyTest tests with default HTML reporting:
```bash
python run_tests.py --runner pytest
```

Run Unittest test suite:
```bash
python run_tests.py --runner unittest
```

Run both test suites:
```bash
python run_tests.py --runner all
```

Execute on a specific browser in headless mode:
```bash
python run_tests.py --runner pytest --browser chrome --headless
```

Filter by test marker (e.g., `smoke`, `login`, `search`, `data_driven`):
```bash
python run_tests.py --runner pytest --marker smoke
```

---

### Option 2: Running Directly via PyTest

Run all tests with self-contained HTML report:
```bash
pytest tests/pytest/ -v --html=reports/report.html --self-contained-html
```

Run only Login tests:
```bash
pytest tests/pytest/test_login.py -v
```

Run only Search tests:
```bash
pytest tests/pytest/test_search.py -v
```

Run specific test markers:
```bash
pytest -m smoke -v
pytest -m data_driven -v
```

---

### Option 3: Running Directly via Unittest

Discover and run all Unittest tests:
```bash
python -m unittest discover -s tests/unittest -p "test_*.py" -v
```

Run specific Unittest module:
```bash
python -m unittest tests/unittest/test_login_unittest.py -v
```
