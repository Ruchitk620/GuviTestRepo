from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    population_count = (
        By.XPATH,
        "//div[contains(@class,'counter-ticker')]"
    )

    def get_population(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.population_count)
        ).text