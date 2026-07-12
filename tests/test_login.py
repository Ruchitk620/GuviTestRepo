import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.excel_utils import ExcelUtils


def test_login(setup):

    driver = setup
    wait = WebDriverWait(driver, 10)

    login = LoginPage(driver)

    excel = ExcelUtils("test_data/LoginData.xlsx")

    rows = excel.get_row_count()

    for row in range(2, rows + 1):

        # Open Login Page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Read Excel Data
        username = excel.get_username(row)
        password = excel.get_password(row)

        # Login
        login.login(username, password)

        try:
            # Wait for Dashboard
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h6[text()='Dashboard']")
                )
            )

            result = "PASS"

            # Logout after successful login
            login.logout()

        except Exception:

            result = "FAIL"

        # Write into Excel
        excel.write_date(row)
        excel.write_time(row)
        excel.write_result(row, result)

    # Save Excel after all rows are completed
    excel.save()
