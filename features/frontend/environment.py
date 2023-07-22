"""Hooks to run before and after certain steps."""

from behave.model import Scenario, Status
from behave_html_formatter.html import HTMLFormatter

from lib.backend.utils import delete_all_boards_via_restapi
from lib.frontend.utils import get_webdriver
from lib.typing import FrontendContext
from lib.utils import get_test_environment_config


def before_all(_: FrontendContext) -> None:
    """Remove all existing boards from trello before test execution."""
    delete_all_boards_via_restapi()


def before_scenario(context: FrontendContext, _: Scenario) -> None:
    """Test setup steps before each test.

    :param context: current test context
    :type context: FrontendContext
    """
    config = get_test_environment_config()
    context.browser = get_webdriver(config["browser"])
    context.browser.get(config["url"]["frontend_base_url"])
    context.board_name = None
    context.board_page = None


def after_scenario(context: FrontendContext, scenario: Scenario) -> None:
    """Test teardown steps before each test.

    :param context: current test context
    :type context: FrontendContext
    :param scenario: current test scenario
    :type scenario: Scenario
    """
    if scenario.status == Status.failed:
        # pylint: disable-next=protected-access
        for formatter in context._runner.formatters:  # noqa: SLF001
            if not isinstance(formatter, HTMLFormatter):
                continue
            formatter.embedding(
                mime_type="image/png",
                data=context.browser.get_screenshot_as_base64(),
                caption="Screenshot",
            )
    if context.board_name and context.board_page:
        context.board_page.delete_board()
    if context.browser is not None:
        context.browser.close()
        context.browser.quit()
        context.browser = None
