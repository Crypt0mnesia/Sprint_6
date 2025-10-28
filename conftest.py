import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data import Settings

@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, Settings.DEFAULT_TIMEOUT)