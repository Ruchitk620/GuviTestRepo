

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


#  Test 1: Parent and Child
def test_parent_child(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    # Example: take Login button
    login = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    # Parent element
    parent = login.find_element(By.XPATH, "..")
    print("Parent tag:", parent.tag_name)

    # First child of parent
    first_child = parent.find_element(By.XPATH, "./*")
    print("First child tag:", first_child.tag_name)

    assert parent is not None


#  Test 2: Sibling
def test_sibling(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    login = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    # Following sibling (next element)
    sibling = login.find_element(By.XPATH, "following-sibling::*")
    print("Sibling tag:", sibling.tag_name)

    assert sibling is not None


#  Test 3: Ancestor Axis
def test_ancestor(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    login = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    ancestors = login.find_elements(By.XPATH, "ancestor::*")
    print("Ancestors count:", len(ancestors))

    assert len(ancestors) > 0


#  Test 4: Following & Preceding
def test_following_preceding(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    login = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    # Following elements
    following = login.find_elements(By.XPATH, "following::*")
    print("Following count:", len(following))

    # Preceding elements
    preceding = login.find_elements(By.XPATH, "preceding::*")
    print("Preceding count:", len(preceding))

    assert len(following) > 0 or len(preceding) > 0
