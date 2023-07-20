"""Test steps to be used by frontend tests."""

# pylint: disable=missing-docstring

from behave import given, then, when  # pylint: disable=no-name-in-module

from lib.frontend.pages.login_page import LoginPage
from lib.typing import FrontendContext
from lib.utils import get_test_environment_config


@given("I am on the Trello homepage")
def iam_on_the_trello_homepage(context: FrontendContext) -> None:
    """Perform login to trello and update the context with homepage."""
    credential = get_test_environment_config()["credentials"]
    context.home_page = LoginPage(context.browser).login(
        credential["email"],
        credential["password"],
    )


@when("I click on create button")
def click_on_create_button(context: FrontendContext) -> None:
    """Click on create button on the homepage."""
    context.home_page.click_on_create()


@when("I select the board option")
def select_board_from_list(context: FrontendContext) -> None:
    """Select board from list of create options."""
    context.home_page.select_board_from_list()


@when('I enter the board name as "{board_name}"')
def enter_a_valid_board_name(
    context: FrontendContext,
    board_name: str,
) -> None:
    """Enter given board in the board name text field."""
    context.board_name = board_name
    context.home_page.enter_board_name(board_name)


@when("I click on create board button")
def click_on_create_board_button(context: FrontendContext) -> None:
    """Click on create board button inside the create board modal."""
    context.board_page = context.home_page.click_on_create_board()


@then('I should see a new board with the name "{board_name}"')
def validate_board_name(
    context: FrontendContext,
    board_name: str,
) -> None:
    """Validate new board name is match with given name."""
    assert context.board_page.get_board_name() == board_name  # noqa: S101


@given('I create a board with name "{board_name}"')
@when('I create a board with name "{board_name}"')
def create_a_board_with_given_name(
    context: FrontendContext,
    board_name: str,
) -> None:
    """Create a board with given name from homepage."""
    context.board_name = board_name
    context.board_page = context.home_page.create_board(board_name)


@given('I have "{num_lists}" lists on the board')
@then('I have "{num_lists}" lists on the board')
def validate_number_of_lists(
    context: FrontendContext,
    num_lists: str,
) -> None:
    """Validate number of lists in the board with given number."""
    assert len(context.board_page.get_all_lists()) == int(  # noqa: S101
        num_lists,
    )


@when("I archive first list item")
def archive_first_list_item(context: FrontendContext) -> None:
    """Archive first list item in the board."""
    context.board_page.archive_first_list()


@when("I permanently delete the board")
def permanently_delete_board(context: FrontendContext) -> None:
    """Delete current board permanently from the workspace."""
    context.board_page.delete_board()
    context.board_name = None


@then('I dont have "{board_name}" board in my workspace')
def validate_number_of_boards(
    context: FrontendContext,
    board_name: str,
) -> None:
    """Validate workspace has no boards."""
    assert (  # noqa: S101
        board_name not in context.board_page.get_all_board_names()
    )
