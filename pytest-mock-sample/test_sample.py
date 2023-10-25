import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Navigate to a webpage and maximize it
    driver.maximize_window()

    # Yield the driver object to the test
    yield driver

    # After the test is done, quit the driver to release resources
    driver.quit

def test_network_error_handling(driver, mocker):
    # Mock the driver.get method to raise a WebDriverException (simulating a network error)
    mocked_get = mocker.patch.object(driver, 'get')
    mocked_get.side_effect = Exception("Network Error")

    # Attempt to navigate to a webpage
    try:
        driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    except Exception as e:
        #Print the exception raise by the mock
        print(e)

        # Assert that the exception message contains "Network Error"
        assert "Network Error" in str(e)
