from typing import Tuple

import pytest

from HW1.tasks.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test_file03.txt", (-20, 15)),
    ],
)
def test_max_min(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
