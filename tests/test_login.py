"""
Task 14 Test Cases
"""
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


# Positive Login
def test_successful_login(setup):

    driver = setup

    login = LoginPage(driver)

    try:
        login.login("ruchitk.ganesh@gmail.com", "Csrockers@1")

        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard")
        )

        assert "dashboard" in driver.current_url.lower()

    except TimeoutException:
        assert False


# Negative Login
def test_unsuccessful_login(setup):

    driver = setup

    login = LoginPage(driver)

    login.login("wronguser", "wrongpassword")

    assert "login" in driver.current_url.lower()


# Username & Password
def test_input_boxes(setup):

    login = LoginPage(setup)

    assert setup.find_element(*login.username).is_displayed()

    assert setup.find_element(*login.password).is_displayed()


# Submit Button
def test_submit_button(setup):

    login = LoginPage(setup)

    assert setup.find_element(*login.login_button).is_enabled()



# Logout Test
def test_logout(setup):

    driver = setup

    login = LoginPage(driver)

    # Login with valid credentials
    login.login(
        "ruchitk.ganesh@gmail.com",
        "Csrockers@1"
    )

    # Logout
    login.click_logout()

    # Validate logout
    assert "login" in driver.current_url.lower()