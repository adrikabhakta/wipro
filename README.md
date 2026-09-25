<div align="center">

# 🧪 Wipro Automation Engineering Portfolio

### Adrika Bhakta
**B.Tech in Computer Science Engineering (AI & ML)**  
Institute of Engineering & Management (IEM), Kolkata

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.49-43B02A?style=flat-square&logo=selenium&logoColor=white)](https://selenium.dev/)
[![PyTest](https://img.shields.io/badge/PyTest-9.1-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org/)
[![GitHub](https://img.shields.io/badge/GitHub-adrikabhakta-181717?style=flat-square&logo=github)](https://github.com/adrikabhakta)

</div>

---

## 👩‍💻 About This Repository

This repository is the complete portfolio of my **Wipro Automation Engineering Capstone Program** — a structured, hands-on journey through modern software test automation using industry-standard tools and frameworks.

It captures everything built, learned, and delivered across four progressive modules and a final Capstone Project, including practical assignments, framework source code, live execution evidence, and professional certifications.

---

## 📁 Repository Structure

```
wipro/
├── 📂 capstone project/        → Capstone 2: Complete Selenium Python E-Commerce Automation Framework
│   ├── pages/                  → Page Object Model (POM) classes
│   ├── tests/                  → PyTest & Unittest test suites (E2E, Login, Search)
│   ├── test_data/              → CSV data-driven test datasets
│   ├── utilities/              → Driver factory, config reader, logger, screenshot utils
│   ├── config/                 → config.ini (URL, browser, timeouts, credentials)
│   ├── reports/                → HTML report, timestamped screenshots, execution logs
│   ├── outcome_screenshots/    → Visual execution proof of E2E browser automation
│   ├── run_tests.py            → Unified CLI test runner
│   ├── pytest.ini              → PyTest configuration & marker registry
│   └── requirements.txt        → Python dependencies
│
├── 📂 assignments/             → Module-wise completed assignment PDFs
│   ├── module 1/               → Core Fundamentals & Advanced User Interactions
│   ├── module 2/               → POM, Data-Driven Testing & PyTest Reporting
│   ├── module 3/               → Python BDD Automation with Behave
│   └── module 4/               → Robot Framework Test Automation
│
└── 📂 certifications/          → Verified Coursera completion certificates
    ├── Python for Automation
    ├── Selenium WebDriver with Python
    └── Test Automation with Playwright & Robot Framework
```

---

## 🚀 Capstone Project: Selenium Python E-Commerce Automation Framework

> **Target Application:** [TutorialsNinja E-Commerce Demo](https://tutorialsninja.com/demo/)

### What Was Built

A production-grade **Selenium WebDriver 4 + Python test automation framework** built on the **Page Object Model (POM)** architecture, supporting both **PyTest** and **Unittest** as dual test runners.

The framework automates and verifies the complete user journey:

```
Login → Verify Login (My Account) → Product Search → Verify Results → Logout → Verify Logout
```

### Framework Highlights

| Feature | Implementation |
| :--- | :--- |
| 🏗️ **Architecture** | Page Object Model (POM) — clean separation of locators, actions and test logic |
| 🔁 **Dual Runners** | Full **PyTest** (fixtures, markers, parametrize) + **Unittest** (setUp/tearDown, subTest) support |
| 📊 **Data-Driven Testing** | CSV-driven login and product search test vectors via `CSVUtils` |
| 📸 **Screenshot Capture** | Auto-captured step screenshots & Base64-embedded failure screenshots in HTML report |
| 📑 **HTML Reporting** | Self-contained `pytest-html` report with environment metadata, duration & embedded images |
| ⚙️ **Configuration** | Centralized `config.ini` — URL, browser, headless toggle, explicit/implicit waits |
| 📋 **Logging** | Dual-target logger (console + `automation.log`) with file:line level detail |
| 🌐 **Cross-Browser** | Chrome, Firefox and Edge support via `DriverFactory` (headed & headless modes) |

### Test Results Summary

```
PyTest Suite   → 13 tests passed | 0 failed | 0 errors | 100% pass rate
Unittest Suite →  6 tests passed | 0 errors | 0 failures
Browser        → Google Chrome (Headed — visible automation)
```

### Page Objects

| Page Class | Responsibility |
| :--- | :--- |
| `BasePage` | Explicit wait wrappers (click, send_keys, text retrieval, element visibility) |
| `HomePage` | Header navigation, search bar, "My Account" dropdown |
| `LoginPage` | Credential entry, form submit, error alert validation |
| `AccountPage` | Dashboard verification, in-account product search, logout trigger |
| `LogoutPage` | Account Logout confirmation header & message verification |
| `SearchPage` | Product results grid, presence checks, no-result message validation |

### Quick Start

```bash
cd "capstone project"
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run E2E user journey test (headed Chrome):
python run_tests.py --runner pytest --marker e2e

# Run full PyTest suite + generate HTML report:
python run_tests.py --runner pytest --open-report

# Run Unittest suite:
python run_tests.py --runner unittest
```

---

## 📚 Module Assignments

Four progressive assignments covering the full automation engineering curriculum:

| Module | Title | Key Technologies | PDF |
| :---: | :--- | :--- | :--- |
| **1** | Core Fundamentals & Advanced User Interactions | Selenium locators, Explicit Waits, Alerts, Web Tables, Iframes, Windows | [📄 View](assignments/module%201/Module_1_Core_Fundamentals_and_Locators.pdf) |
| **2** | POM, Data-Driven Testing & PyTest Reporting | Page Object Model, CSV DDT, `conftest.py`, `pytest-html` | [📄 View](assignments/module%202/Module_2_Selenium_POM_DDT_PyTest_Reporting.pdf) |
| **3** | Python BDD Automation with Behave | Gherkin Feature Files, Step Definitions, Behave + Selenium POM | [📄 View](assignments/module%203/Module_3_Python_BDD_Selenium_Behave_Framework.pdf) |
| **4** | Robot Framework Test Automation | Robot Framework syntax, Custom Python libraries, Pabot, Tags & Reporting | [📄 View](assignments/module%204/Module_4_Robot_Framework_Test_Automation.pdf) |

---

## 🎓 Certifications

All certificates are Coursera-verified and available for public validation:

| Certificate | Issued By | Date | Verify |
| :--- | :--- | :--- | :--- |
| 🏅 **Python for Automation** | Madecraft via Coursera | Sep 10, 2026 | [🔗 Verify](https://coursera.org/verify/5I2BB260JRGW) |
| 🏅 **Selenium WebDriver with Python** | Whizlabs via Coursera | Sep 18, 2026 | [🔗 Verify](https://coursera.org/verify/5FCJ8Z488PB9) |
| 🏅 **Test Automation with Playwright (Python) & Robot Framework** | Coursera | Sep 25, 2026 | [🔗 Verify](https://coursera.org/verify/0K4FI2HN5OBU) |

📁 [View all certificate PDFs →](certifications/)

---

## 🛠️ Technology Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/-Selenium%20WebDriver-43B02A?style=flat-square&logo=selenium&logoColor=white)
![PyTest](https://img.shields.io/badge/-PyTest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Robot Framework](https://img.shields.io/badge/-Robot%20Framework-000000?style=flat-square&logo=robotframework&logoColor=white)
![Behave](https://img.shields.io/badge/-Behave%20BDD-00A86B?style=flat-square)
![Playwright](https://img.shields.io/badge/-Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)
![Chrome](https://img.shields.io/badge/-Chrome%20WebDriver-4285F4?style=flat-square&logo=googlechrome&logoColor=white)

---

## 👤 Author

**Adrika Bhakta**
- 🎓 B.Tech CSE (AI & ML) — IEM Kolkata
- 💻 Automation Engineer | Python Developer
- 🌐 [GitHub: adrikabhakta](https://github.com/adrikabhakta)

---

<div align="center">
<sub>Built with ❤️ as part of the Wipro Automation Engineering Capstone Program</sub>
</div>
