# -------------------- Task 11: GUVI Automation --------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open GUVI
driver.get("https://www.guvi.in/")
driver.maximize_window()
time.sleep(5)
# Click Login button
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)

# Check URL
print("Current URL:", driver.current_url)

# Enter credentials (use your own)
driver.find_element(By.ID, "email").send_keys("test_email")
driver.find_element(By.ID, "password").send_keys("test_password")

# Click Login button
driver.find_element(By.XPATH, "//a[@id='login-btn']").click()



print("Login attempted successfully")

driver.quit()
