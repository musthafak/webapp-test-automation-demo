"""Hooks to run before and after certain steps."""

# pylint: disable=missing-docstring

from lib.backend.utils import delete_board_via_restapi
from lib.typing import BackendContext
from lib.utils import get_tests_config


def before_scenario(context: BackendContext, *_: tuple) -> None:
    """Test setup steps before each test."""
    config = get_tests_config()
    context.base_url = config["url"]["backend_base_url"]
    context.board_id = ""
    context.non_existing_board_id = ""
    context.response = None


def after_scenario(context: BackendContext, *_: tuple) -> None:
    """Test teardown steps before each test."""
    if not context.board_id:
        return
    delete_board_via_restapi(context.board_id)
