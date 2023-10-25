from selenium.webdriver.common.by import By
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from time import sleep
import pytest
import configparser
import os

scenarios('../features/simple_form_demo.feature')

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

@pytest.fixture()
def driver():
    username = os.getenv("LT_USERNAME")
    accessKey = os.getenv("LT_ACCESS_KEY")

    gridUrl = config.get('CLOUDGRID', 'grid_url')

    web_driver = webdriver.ChromeOptions()
    platform = config.get('ENV', 'platform')
    browser_name = config.get('ENV', 'browser_name')

    lt_options = {
        "user": username,
        "accessKey": accessKey,
        "build": config.get('CLOUDGRID', 'build_name'),
        "name": config.get('CLOUDGRID', 'test_name'),
        "platformName": platform,
        "w3c": config.get('CLOUDGRID', 'w3c'),
        "browserName": browser_name,
        "browserVersion": config.get('CLOUDGRID', 'browser_version'),
        "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
		"visual": True
    }

    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{accessKey}@{gridUrl}"
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

@given("the user is on the Simple Form Demo page")
def open_simple_form_demo(driver):
    driver.get(config.get('WEBSITE', 'url'))

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