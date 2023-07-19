"""Utils module."""

import json
from pathlib import Path
from typing import Any

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_tests_config() -> dict[str, Any]:
    """Return tests config dictionary.

    :return: tests config dictionary
    :rtype: dict[str, str]
    """
    return json.loads(
        (Path(__file__).parent / ".." / "configs" / "config.json").read_text(
            encoding="utf-8",
        ),
    )


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
