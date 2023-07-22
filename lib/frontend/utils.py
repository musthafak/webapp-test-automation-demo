"""Frontend utils module."""

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_webdriver(browser: str) -> WebDriver:
    """Get webdriver instance based on the config file.

    :return: webdriver instance
    :rtype: WebDriver
    """
    web_drivers = {
        "firefox": webdriver.Firefox,
        "chrome": webdriver.Chrome,
        "edge": webdriver.Edge,
    }
    if browser in web_drivers:
        driver = web_drivers[browser]()
        driver.maximize_window()
        return driver
    error_msg = f"Unsupported browser type: {browser}"
    raise ValueError(error_msg)
