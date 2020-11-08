import string
from typing import List

import pytest
from task05 import custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        (
            (string.ascii_lowercase, "g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
        (([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4, 9, 2), [4, 6, 8]),
    ],
)
def test_custom_range(value, expected_result: List):
    actual_result = custom_range(*value)

    assert actual_result == expected_result
