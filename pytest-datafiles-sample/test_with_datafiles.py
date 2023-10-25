from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import json

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Navigate to a webpage
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    
    # Yielding the driver object to the test
    yield driver
    
    # Quitting the driver after the test
    driver.quit

@pytest.mark.datafiles('test_data.json')
def test_simple_form_demo(driver, datafiles):
    # Find an input element by its ID
    input_element = driver.find_element(By.ID, "user-message")
    
    # Find a button element by its ID and click on it
    button_element = driver.find_element(By.ID, "showInput")

    # Find a message element by its ID
    message_element = driver.find_element(By.ID, "message")
   
    # Looping through the list of scenario files provided by pytest-datafiles
    for scenario_file in datafiles.iterdir():
        with scenario_file.open() as file:

            # Loading the JSON data from the file
            scenario_data = json.load(file)

            # Looping through the list of scenario inside a scenario files
            for data in scenario_data:
                # Clean the input field before typing the message
                input_element.clear()     

                # Entering the message from the data into the input field
                input_element.send_keys(data["message"])

                # Clicking the button to display the message
                button_element.click()

                # Asserting that the displayed message matches the expected message from the data
                assert message_element.text == data["message"]