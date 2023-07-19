"""Hooks to run before and after certain steps."""

# pylint: disable=missing-docstring

import os

from xvfbwrapper import Xvfb

from lib.typing import FrontendContext
from lib.utils import get_tests_config, get_webdriver


def before_scenario(context: FrontendContext, *_: tuple) -> None:
    """Test setup steps before each test."""
    config = get_tests_config()
    if os.environ.get("IS_BROWSER_INSIDE_CONTAINER") == "TRUE":
        context.vdisplay = Xvfb(width=1920, height=1080)
        context.vdisplay.start()
    else:
        context.vdisplay = None
    context.browser = get_webdriver(
        config["driver"]["browser"],
    )
    context.browser.get(config["url"]["frontend_base_url"])
    context.board_name = None
    context.board_page = None


def after_scenario(context: FrontendContext, *_: tuple) -> None:
    """Test teardown steps before each test."""
    if context.board_name and context.board_page:
        context.board_page.delete_board()
    if context.browser is not None:
        context.browser.close()
        context.browser.quit()
        context.browser = None
    if context.vdisplay is not None:
        context.vdisplay.stop()
        context.vdisplay = None
