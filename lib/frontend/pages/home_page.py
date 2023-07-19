"""Home page."""

from selenium.webdriver.common.by import By

from lib.frontend.pages.base_page import BasePage
from lib.frontend.pages.board_page import BoardPage


class _SELECTORS:  # pylint: disable=too-few-public-methods
    """Home page."""

    CREATE_BUTTON = (
        By.CSS_SELECTOR,
        '[data-testid="header-create-menu-button"]',
    )
    CREATE_BOARD_OPTION = (
        By.CSS_SELECTOR,
        '[data-testid="header-create-board-button"]',
    )
    BOARD_TITLE_INPUT = (
        By.CSS_SELECTOR,
        '[data-testid="create-board-title-input"]',
    )
    CREATE_BOARD_BUTTON = (
        By.CSS_SELECTOR,
        '[data-testid="create-board-submit-button"]',
    )


class HomePage(BasePage):
    """Home page."""

    def click_on_create(self) -> None:
        """Click on create board dropdown button."""
        self._click_element(_SELECTORS.CREATE_BUTTON)

    def select_board_from_list(self) -> None:
        """Click on board dropdown list."""
        self._click_element(_SELECTORS.CREATE_BOARD_OPTION)

    def enter_board_name(self, board_name: str) -> None:
        """Enter board name in the text field.

        :param board_name: name of the board
        :type board_name: str
        """
        self._send_keys_to_element(_SELECTORS.BOARD_TITLE_INPUT, board_name)

    def click_on_create_board(self) -> BoardPage:
        """Click on a create and it will take you to board page.

        :return: board page instance
        :rtype: BoardPage
        """
        self._click_element(_SELECTORS.CREATE_BOARD_BUTTON)
        return BoardPage(self._driver)

    def create_board(self, board_name: str) -> BoardPage:
        """Create a board with given board name.

        :param board_name: name of the board
        :type board_name: str
        :return: board page instance
        :rtype: BoardPage
        """
        self.click_on_create()
        self.select_board_from_list()
        self.enter_board_name(board_name)
        return self.click_on_create_board()
