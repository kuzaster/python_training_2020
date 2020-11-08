import os

import pytest
from task01 import get_most_common_non_ascii_char


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "ä"),
        (os.path.join(os.path.dirname(__file__), "data1.txt"), "ü"),
    ],
)
def test_major_minor(value: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(value)

    assert actual_result == expected_result
