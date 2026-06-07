import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive(setup):
    driver = setup

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    assert "inventory" in driver.current_url

def test_negative(setup):
    driver = setup

    driver.find_element(By.ID, "user-name").send_keys("Rajkumar")
    driver.find_element(By.ID, "password").send_keys("pavithragowda")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Check error message
    error = driver.find_element(By.XPATH, "//h3").text
    assert "Epic sadface" in error
    print( error)
