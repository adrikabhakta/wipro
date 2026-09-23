#!/usr/bin/env python3
"""
Unified Test Runner Script for Selenium Automation Framework.
Provides single-entry CLI execution for both PyTest and Unittest suites
with automatic reporting and logging.
"""

import argparse
import os
import sys
import subprocess
import unittest
import pytest
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Selenium Python Automation Framework Test Runner (PyTest & Unittest)"
    )
    parser.add_argument(
        "--runner",
        choices=["pytest", "unittest", "all"],
        default="pytest",
        help="Test runner framework to invoke (default: pytest)"
    )
    parser.add_argument(
        "--browser",
        choices=["chrome", "firefox", "edge"],
        default=None,
        help="Target browser (overrides config.ini)"
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        help="Execute tests in headless (invisible) browser mode"
    )
    parser.add_argument(
        "--marker",
        type=str,
        default=None,
        help="PyTest marker to filter tests (e.g., 'smoke', 'login', 'search', 'data_driven')"
    )
    parser.add_argument(
        "--report",
        type=str,
        default="reports/report.html",
        help="Path for generated HTML test report (default: reports/report.html)"
    )
    parser.add_argument(
        "--open-report",
        action="store_true",
        default=False,
        help="Automatically open the HTML report in the default browser after execution"
    )

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    os.chdir(project_root)

    # Ensure required report subdirectories exist
    (project_root / "reports" / "screenshots").mkdir(parents=True, exist_ok=True)
    (project_root / "reports" / "logs").mkdir(parents=True, exist_ok=True)

    exit_code = 0

    headless_str = "true" if args.headless else "false"

    print("=" * 70)
    print(" SELENIUM PYTHON AUTOMATION TEST RUNNER")
    print(f" Framework : Page Object Model (POM)")
    print(f" Target    : https://tutorialsninja.com/demo/")
    print(f" Runner    : {args.runner.upper()}")
    print(f" Mode      : {'HEADLESS' if args.headless else 'HEADED (Visible Browser)'}")
    print("=" * 70)

    if args.runner in ("pytest", "all"):
        print("\n>>> Launching PyTest Test Suite with HTML Reporting...\n")
        pytest_args = [
            str(project_root / "tests" / "pytest"),
            "-v",
            "-s",
            f"--html={args.report}",
            "--self-contained-html",
            "--headless", headless_str,
        ]

        if args.browser:
            pytest_args.extend(["--browser", args.browser])
        if args.marker:
            pytest_args.extend(["-m", args.marker])

        code = pytest.main(pytest_args)
        if code != 0:
            exit_code = code

        print(f"\n[+] PyTest execution completed. HTML Report: {project_root / args.report}")

    if args.runner in ("unittest", "all"):
        print("\n>>> Launching Unittest Test Suite...\n")
        loader = unittest.TestLoader()
        start_dir = str(project_root / "tests" / "unittest")
        suite = loader.discover(start_dir=start_dir, pattern="test_*.py")

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if not result.wasSuccessful():
            exit_code = 1

        print(f"\n[+] Unittest execution completed. Tests run: {result.testsRun}, "
              f"Errors: {len(result.errors)}, Failures: {len(result.failures)}")

    if args.open_report:
        report_file = project_root / args.report
        if report_file.exists():
            print(f"\n[+] Opening HTML report in browser: {report_file}")
            subprocess.run(["open", str(report_file)])

    print("\n" + "=" * 70)
    print(f" ALL EXECUTIONS COMPLETED (Exit Code: {exit_code})")
    print("=" * 70)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
