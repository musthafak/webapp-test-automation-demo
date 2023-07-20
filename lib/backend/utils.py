"""Backend API testing helper functions."""

import json

import requests

from lib.utils import get_test_environment_config

_CONFIG = get_test_environment_config()


def make_http_request(
    method: str,
    url: str,
    payload: str,
) -> requests.Response:
    """Make HTTP request to given url.

    :param method: request method
    :type method: str
    :param url: request url
    :type url: str
    :param payload: request payload
    :type payload: str
    :return: response from the server
    :rtype: requests.Response
    """
    return requests.request(
        method,
        url,
        headers={"Content-Type": "application/json"},
        data=payload,
        timeout=10,
    )


def get_api_token_and_key() -> tuple[str, str]:
    """Get API athentication token and key.

    :return: authentication key, token
    :rtype: tuple[str, str]
    """
    credentials = _CONFIG["credentials"]
    return credentials["key"], credentials["token"]


def _make_http_request_with_credentials(
    method: str,
    url: str,
) -> requests.Response:
    base_url = _CONFIG["url"]["backend_base_url"]
    return make_http_request(
        method,
        f"{base_url}/{url}",
        json.dumps(
            {
                "key": _CONFIG["credentials"]["key"],
                "token": _CONFIG["credentials"]["token"],
            },
        ),
    )


def delete_board_via_restapi(board_id: str) -> None:
    """Delete board with given board ID.

    :param board_id: board id
    :type board_id: str
    """
    _make_http_request_with_credentials(
        "DELETE",
        f"boards/{board_id}",
    ).raise_for_status()


def delete_all_boards_via_restapt() -> None:
    """Delete all boards on the trello via restapi."""
    boards_response = _make_http_request_with_credentials(
        "GET",
        "members/me/boards",
    )
    boards_response.raise_for_status()
    for board in boards_response.json():
        _make_http_request_with_credentials(
            "DELETE",
            f"boards/{board['id']}",
        ).raise_for_status()
