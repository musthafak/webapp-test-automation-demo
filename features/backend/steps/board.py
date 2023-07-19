"""Test steps to be used by frontend tests."""

# pylint: disable=missing-docstring

import json

from behave import given, then, when  # pylint: disable=no-name-in-module

from lib.backend.utils import get_api_token_and_key, make_http_request
from lib.typing import BackendContext


def _get_payload(context: BackendContext, payload: str) -> str:
    return json.dumps(
        json.loads(payload or "{}")
        | {
            "token": context.token,
            "key": context.api_key,
        },
    )


@given("I have a valid API key and token")
def setup_valid_key_and_token(context: BackendContext) -> None:
    """Set up valid API key and token for authentication."""
    context.api_key, context.token = get_api_token_and_key()


@when('I send a {method} request to "{endpoint}"')
def make_a_request_without_payload(
    context: BackendContext,
    method: str,
    endpoint: str,
) -> None:
    """Make a request to the given server endpoint via given method."""
    url = context.base_url + endpoint.format(
        boardId=context.board_id,
        nonExistingBoardId=context.non_existing_board_id,
    )
    context.response = make_http_request(
        method,
        url,
        _get_payload(context, None),
    )


@when('I send a {method} request to "{endpoint}" with the payload')
def make_a_request_with_payload(
    context: BackendContext,
    method: str,
    endpoint: str,
) -> None:
    """Make a request to the given endpoint with payload."""
    url = context.base_url + endpoint.format(
        boardId=context.board_id,
        nonExistingBoardId=context.non_existing_board_id,
    )
    context.response = make_http_request(
        method,
        url,
        _get_payload(context, _get_payload(context, context.text)),
    )


@then("the response status code should be {status_code}")
def verify_response_code(context: BackendContext, status_code: str) -> None:
    """Verify server respose code is equal to given status code."""
    assert context.response.status_code == int(  # noqa: S101
        status_code,
    ), context.response.status_code


@then("the response body should contain the board ID")
def verify_response_body_has_board_id(context: BackendContext) -> None:
    """Verify respose json has board ID."""
    response_json = context.response.json()
    assert "id" in response_json  # noqa: S101
    context.board_id = response_json["id"]


@then("the board should be created successfully")
def verify_board_created_successfully(context: BackendContext) -> None:
    """Verify the board is created successfully on the server."""
    response_json = context.response.json()
    assert "id" in response_json  # noqa: S101
    assert "name" in response_json  # noqa: S101
    assert response_json["name"] == "Project A"  # noqa: S101


@then("the response body should contain the board details")
def verify_reponse_contains_board_details(context: BackendContext) -> None:
    """Verify json response contains board details."""
    response_json = context.response.json()
    assert "id" in response_json  # noqa: S101
    assert "name" in response_json  # noqa: S101
    assert response_json["id"] == context.board_id  # noqa: S101


@then('the board name should be updated to "{updated_name}"')
def verify_board_name_is_updated(
    context: BackendContext,
    updated_name: str,
) -> None:
    """Verify board name is updated to given name."""
    url = f"{context.base_url}/boards/{context.board_id}"
    response_json = make_http_request(
        "GET",
        url,
        _get_payload(context, None),
    ).json()
    assert response_json["name"] == updated_name  # noqa: S101


@then("the board should be deleted successfully")
def verify_board_is_deleted_successfully(context: BackendContext) -> None:
    """Verify board is deleted by checking the respose code."""
    response = make_http_request(
        "GET",
        f"{context.base_url}/boards/{context.board_id}",
        _get_payload(context, None),
    )
    assert response.status_code == 404  # noqa: S101,PLR2004
    context.board_id = None


@then('the response body should contain "{error_message}"')
def verify_response_had_error_message(
    context: BackendContext,
    error_message: str,
) -> None:
    """Verify the respose contain given error message."""
    assert error_message in context.response.text  # noqa: S101


@given("I have a board ID")
def create_a_board(context: BackendContext) -> None:
    """Set up a valid board ID for subsequent steps."""
    url = f"{context.base_url}/boards"
    context.board_id = make_http_request(
        "POST",
        url,
        _get_payload(context, '{ "name": "Project X" }'),
    ).json()["id"]


@given("I have a non-existing board ID")
def setup_board_id_non_existing(context: BackendContext) -> None:
    """Set up a non-existing board ID for subsequent steps."""
    context.api_key, context.token = get_api_token_and_key()
    context.non_existing_board_id = "NON_EXISTING_BOARD_ID"
