"""Frontend utils module."""

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_webdriver(browser: str) -> WebDriver:
    """Get webdriver instance based on the config file.

    :return: webdriver instance
    :rtype: WebDriver
    """
    if browser == "firefox":
        driver: WebDriver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        error_msg = f"Invalid browser type: {browser}"
        raise ValueError(error_msg)
    driver.maximize_window()
    return driver
