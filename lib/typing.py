"""Type definitions for different classes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from behave.runner import Context

if TYPE_CHECKING:
    import requests
    from selenium.webdriver.remote.webdriver import WebDriver
    from xvfbwrapper import Xvfb

    from lib.frontend.pages.board_page import BoardPage
    from lib.frontend.pages.home_page import HomePage
    from lib.frontend.pages.login_page import LoginPage


class FrontendContext(Context):  # pylint: disable=too-few-public-methods
    """Frontend context class definition."""

    browser: WebDriver
    home_page: HomePage
    login_page: LoginPage
    board_page: BoardPage
    board_name: str
    vdisplay: Xvfb


class BackendContext(Context):  # pylint: disable=too-few-public-methods
    """Frontend context class definition."""

    text: str
    token: str
    api_key: str
    base_url: str
    board_id: str
    response: requests.Response
    non_existing_board_id: str
