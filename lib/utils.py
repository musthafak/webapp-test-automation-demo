"""Common utils module."""

import json
from pathlib import Path
from typing import Any


def get_test_environment_config() -> dict[str, Any]:
    """Get test environment configuration dictionary.

    :return: tests config dictionary
    :rtype: dict[str, str]
    """
    return json.loads(
        (
            Path(__file__).parent / ".." / "configs" / "test_environment.json"
        ).read_text(encoding="utf-8"),
    )
