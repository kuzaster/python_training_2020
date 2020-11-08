import os

import pytest
from task01 import count_non_ascii_chars


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 2972),
        (os.path.join(os.path.dirname(__file__), "data1.txt"), 6),
    ],
)
def test_major_minor(value: str, expected_result: int):
    actual_result = count_non_ascii_chars(value)

    assert actual_result == expected_result
