from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Navigate to a webpage
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    
    yield driver
    
    driver.quit

def test_simple_form_demo(driver):
    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("Basic Pytest test")

    # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()

    # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")

    assert element.text == "Basic Pytest test"