"""Backend API testing helper functions."""

import json

import requests

from lib.utils import get_tests_config


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
    credentials = get_tests_config()["credentials"]["backend"]
    return credentials["key"], credentials["token"]


def delete_board_via_restapi(board_id: str) -> None:
    """Delete board with given board ID.

    :param board_id: board id
    :type board_id: str
    """
    config = get_tests_config()
    base_url = config["url"]["backend_base_url"]
    credentials = config["credentials"]["backend"]
    make_http_request(
        "DELETE",
        f"{base_url}/boards/{board_id}",
        json.dumps(
            {
                "key": credentials["key"],
                "token": credentials["token"],
            },
        ),
    ).raise_for_status()
