from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Your existing methods
    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ADD THIS METHOD
    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Logout']")
            )
        ).click()
