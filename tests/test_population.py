import pytest
import time

from pages.population_page import PopulationPage


def test_live_population(setup):

    driver = setup

    population = PopulationPage(driver)

    print("\nPress CTRL + C to stop...\n")

    try:
        while True:
            count = population.get_population()
            print("Current World Population:", count)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user.")