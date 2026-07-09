import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

GECKO_PATH = r"C:\GeckoDriver\geckodriver.exe"

@pytest.fixture
def driver():
    service = Service(executable_path=GECKO_PATH)
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5) 
    yield driver
    driver.quit()