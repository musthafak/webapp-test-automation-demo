"""Login page."""

from selenium.webdriver.common.by import By

from lib.frontend.pages.base_page import BasePage
from lib.frontend.pages.home_page import HomePage


class _SELECTORS:  # pylint: disable=too-few-public-methods
    """Login page."""

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        '[data-testid="login"]',
    )
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        '[placeholder="Enter email"]',
    )
    CONTINUE_BUTTON = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (By.ID, "login-submit")


class LoginPage(BasePage):  # pylint: disable=too-few-public-methods
    """Login page."""

    def login(self, email: str, password: str) -> HomePage:
        """Login to the website.

        :param email: email address
        :type email: str
        :param password: password
        :type password: str
        """
        self._click_element(_SELECTORS.LOGIN_BUTTON)
        self._send_keys_to_element(_SELECTORS.EMAIL_INPUT, email)
        self._click_element(_SELECTORS.CONTINUE_BUTTON)
        self._send_keys_to_element(_SELECTORS.PASSWORD_INPUT, password)
        self._click_element(_SELECTORS.LOGIN_SUBMIT_BUTTON)
        return HomePage(self._driver)
