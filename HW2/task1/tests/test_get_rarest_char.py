import os

import pytest
from task01 import get_rarest_char


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "›"),
        (os.path.join(os.path.dirname(__file__), "data1.txt"), "W"),
    ],
)
def test_major_minor(value: str, expected_result: str):
    actual_result = get_rarest_char(value)

    assert actual_result == expected_result
