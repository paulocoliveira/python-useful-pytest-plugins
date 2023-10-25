from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pytest_check import check
import time


@pytest.fixture()
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Navigate to a webpage and maximize it
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.maximize_window()

    # Yield the driver object to the test
    yield driver

    # After the test is done, quit the driver to release resources
    driver.quit

def test_1(driver):

    # Define a list of messages
    message_list = ["Using Pytest", "Using Selenium", "Using Pytest Selenium for testing"]

    # Find an input element by its ID
    input_element = driver.find_element(By.ID, "user-message")
    
    # Find a button element by its ID and click on it
    button_element = driver.find_element(By.ID, "showInput")

    # Find a message element by its ID
    message_element = driver.find_element(By.ID, "message")

    # Loop through the search queries
    for message in message_list:
        # Clean the input field and type the message
        input_element.clear()       
        input_element.send_keys(message)

        # Click in the button
        button_element.click()

        # Use pytest-check to perform assertions
        with check:
            assert len(message_element.text) > 50
            assert message_element.text == message
        
        time.sleep(3)