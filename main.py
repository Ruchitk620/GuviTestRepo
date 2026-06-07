import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#open the browser
driver = webdriver.Chrome()

#open the website
driver.get("https://www.saucedemo.com/")
time.sleep(5)

print("Title: ",driver.title) # prints the title
print("URL: ",driver.current_url) # prints the URL

#login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# get the page content
content = driver.page_source

with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Page content saved successfully!")

# Close browser
driver.quit()


