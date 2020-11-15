import os

import pytest
from task01 import count_punctuation_chars


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 5475),
        (os.path.join(os.path.dirname(__file__), "data1.txt"), 8),
    ],
)
def test_major_minor(value: str, expected_result: int):
    actual_result = count_punctuation_chars(value)

    assert actual_result == expected_result
