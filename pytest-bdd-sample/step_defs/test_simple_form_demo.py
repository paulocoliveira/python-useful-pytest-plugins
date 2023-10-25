from selenium.webdriver.common.by import By
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from time import sleep
import pytest

scenarios('../features/simple_form_demo.feature')

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@given("the user is on the Simple Form Demo page")
def open_simple_form_demo(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

@when(parsers.parse('the user enters the message "{message}" in the input field'))
def enter_message(driver, message):
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys(message)

@when('clicks the Show Message button')
def click_show_message_button(driver):
    element = driver.find_element(By.ID, "showInput")
    element.click()

@then(parsers.parse('the user should see the message "{message}"'))
def verify_message(driver, message):
    element = driver.find_element(By.ID, "message")
    assert element.text == message
    sleep(5)