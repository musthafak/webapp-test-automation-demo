"""Board page."""

from selenium.webdriver.common.by import By

from lib.frontend.pages.base_page import BasePage


class _SELECTORS:  # pylint: disable=too-few-public-methods
    BOARD_NAME_DISPLAY = (
        By.CSS_SELECTOR,
        r'[data-testid="board-name-container"]',
    )
    BOARDS_LEFT_SIDE_MENU_OPTION = (
        By.CSS_SELECTOR,
        '[data-testid="open-boards-link"]',
    )
    BOARD_TILE_DETAILS_NAME = (
        By.CSS_SELECTOR,
        '[class="board-tile-details-name"]',
    )
    OPTIONS_MENU = (By.CSS_SELECTOR, r'[aria-label="Show menu"]')
    CLOSE_BOARD_MENU_ITEM = (By.CSS_SELECTOR, ".js-close-board")
    CLOSE_BOARD_CONFIRM_BUTTON = (
        By.CSS_SELECTOR,
        r'[class="js-confirm full nch-button nch-button--danger"]',
    )
    PERMANENTLY_DELETE_BOARD = (
        By.CSS_SELECTOR,
        r'[data-testid="close-board-delete-board-button"]',
    )
    CONFIRM_PERMANENTLY_DELETE_BOARD = (
        By.CSS_SELECTOR,
        r'[data-testid="close-board-delete-board-confirm-button"]',
    )
    LIST_ACTIONS_MENU = (
        By.CSS_SELECTOR,
        (
            r'[class="list-header-extras-menu js-open-list-menu icon-sm'
            r' icon-overflow-menu-horizontal"]'
        ),
    )
    ARCHIVE_THIS_LIST = (By.CSS_SELECTOR, '[class="js-close-list"]')
    LIST_ITEM_HEADER_NAME = (
        By.CSS_SELECTOR,
        '[class="list-header-name mod-list-name js-list-name-input"]',
    )


class BoardPage(BasePage):
    """Board page."""

    def archive_first_list(self) -> None:
        """Archive first item in the board."""
        self._click_element(_SELECTORS.LIST_ACTIONS_MENU)
        self._click_element(_SELECTORS.ARCHIVE_THIS_LIST)

    def get_board_name(self) -> str:
        """Return board name.

        :return: board name
        :rtype: str
        """
        return self._wait_for_element(_SELECTORS.BOARD_NAME_DISPLAY).text

    def get_all_lists(self) -> list[str]:
        """Get name of all list items.

        :return: name of all lists
        :rtype: list[str]
        """
        self._wait_for_element(_SELECTORS.LIST_ITEM_HEADER_NAME)
        return [
            element.text
            for element in self._find_elements(
                _SELECTORS.LIST_ITEM_HEADER_NAME,
            )
        ]

    def delete_board(self) -> None:
        """Delete current board."""
        self._click_element(_SELECTORS.OPTIONS_MENU)
        self._click_element(_SELECTORS.CLOSE_BOARD_MENU_ITEM)
        self._click_element(_SELECTORS.CLOSE_BOARD_CONFIRM_BUTTON)
        self._click_element(_SELECTORS.PERMANENTLY_DELETE_BOARD)
        self._click_element(_SELECTORS.CONFIRM_PERMANENTLY_DELETE_BOARD)

    def get_all_board_names(self) -> list[str]:
        """Get all board names from board page.

        :return: list of available board names
        :rtype: list[str]
        """
        self._click_element(_SELECTORS.BOARDS_LEFT_SIDE_MENU_OPTION)
        return [
            element.text
            for element in self._find_elements(
                _SELECTORS.BOARD_TILE_DETAILS_NAME,
            )
        ]
