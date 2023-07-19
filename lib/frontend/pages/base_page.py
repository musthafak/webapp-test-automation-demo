"""Base page to be used by all pages."""


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:  # pylint: disable=too-few-public-methods
    """Base page to be used by all pages."""

    def __init__(self, driver: WebDriver) -> None:
        """Initialize base page."""
        self._driver = driver

    def _wait_for_element(
        self,
        locator: tuple[str, str],
        timeout: int = 10,
    ) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator),
        )

    def _click_element(
        self,
        locator: tuple[str, str],
        timeout: int = 10,
    ) -> None:
        WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator),
        ).click()

    def _send_keys_to_element(
        self,
        locator: tuple[str, str],
        text: str,
        timeout: int = 10,
    ) -> None:
        element = self._wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def _find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._driver.find_elements(locator[0], locator[1])
