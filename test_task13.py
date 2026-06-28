"""
Task 13
Drag and Drop using Selenium ActionChains
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()
    yield driver
    driver.quit()


# Positive Test
def test_drag_drop_positive(setup):
    driver = setup

    # Switch to iframe
    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    # Verify drop happened
    assert target.text == "Dropped!"

    print("Drag and Drop Successful")


# Negative Test
def test_drag_drop_negative(setup):
    driver = setup

    # Switch to iframe
    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)

    target = driver.find_element(By.ID, "droppable")

    # Without dragging, verify text is still "Drop here"
    assert target.text == "Drop here"

    print("Drag and Drop not performed")
