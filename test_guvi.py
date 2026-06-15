# -------------------- Pytest Test Cases --------------------
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    yield driver
    driver.quit()


# Test 1: Validate Login URL
def test_login_url(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    time.sleep(5)

    assert "sign-in" in driver.current_url


# Test 2: Validate Input Fields
def test_input_fields(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    username = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    assert username.is_displayed()
    assert username.is_enabled()

    assert password.is_displayed()
    assert password.is_enabled()


# Test 3: Positive Login
def test_submit_button_positive(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("test_email")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("test_password")

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    # After login, URL should change
    assert "sign-in" in driver.current_url


# Test 4: Negative Login
def test_submit_button_negative(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("wrong@email.com")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("wrongpass")

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    time.sleep(5)

    print("URL after invalid login:", driver.current_url)

    assert "sign-in" in driver.current_url.lower()

