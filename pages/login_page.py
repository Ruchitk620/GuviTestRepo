"""
Page Object Model for Zen Portal Login Page
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username = (By.ID, ":r1:")
        self.password = (By.ID, ":r2:")
        self.login_button = (By.XPATH, "//button[text()='Sign in']")

        # Close popup after login
        self.close_popup = (
            By.XPATH,
            "//button[@class='custom-close-button']"
        )

        # Profile icon
        self.profile_icon = (
            By.ID,
            "profile-click-icon"
        )

        # Logout button
        self.logout_button = (
            By.XPATH,
            "//div[@class='user-avatar-menu' and text()='Log out']"
        )

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def close_notification(self):
        self.wait.until(
            EC.element_to_be_clickable(self.close_popup)
        ).click()

    def click_logout(self):
        # Close popup
        self.wait.until(
            EC.element_to_be_clickable(self.close_popup)
        ).click()

        time.sleep(2)

        # Open profile menu
        self.wait.until(
            EC.element_to_be_clickable(self.profile_icon)
        ).click()

        time.sleep(2)

        # Click logout
        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

        time.sleep(5)