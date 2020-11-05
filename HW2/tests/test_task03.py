from typing import Any, List

import pytest

from HW2.tasks.task03 import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ],
)
def test_combination(value: List[Any], expected_result: List[List]):
    actual_result = combinations(*value)

    assert actual_result == expected_result
