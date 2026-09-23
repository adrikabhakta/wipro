# Test Automation Outcome Screenshots

This directory contains the visual execution outcomes and HTML test report screenshots for the **Selenium Python E-Commerce Automation Framework (Capstone 2)**.

---

## 1. PyTest HTML Execution Report Overview
Displays the test report showing all test cases passed with 0 failures, duration, and execution metadata.

![01_pytest_html_report_overview](01_pytest_html_report_overview.png)

---

## 2. Step 1: Login Page Navigation
User navigates to the Returning Customer login page (`index.php?route=account/login`).

![02_e2e_login_page](02_e2e_login_page.png)

---

## 3. Step 2: Login Verified (My Account Dashboard)
User logs in with valid credentials, verifying arrival on the authenticated My Account dashboard.

![03_e2e_account_dashboard_verified](03_e2e_account_dashboard_verified.png)

---

## 4. Step 3: Product Search ("MacBook") Verified
Product search query `MacBook` executed from the header, returning matching product results.

![04_e2e_search_macbook_verified](04_e2e_search_macbook_verified.png)

---

## 5. Step 4: Account Logout Verified
User clicks Logout, asserting the Account Logout confirmation header and message.

![05_e2e_account_logout_verified](05_e2e_account_logout_verified.png)

---

## 6. Negative Test: No Product Found Message Verified
Searching for a non-existent item correctly displays `"There is no product that matches the search criteria."`

![06_search_no_product_found_verified](06_search_no_product_found_verified.png)
