from typing import List

import pytest

from HW1.tasks.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([0, 1], [1, -1], [0, 2], [2, -2]), 2),
        (([0, 1], [2, 3], [4, 5], [6, 7]), 0),
        (([0, 1, -2], [2, 3, -4], [4, 5, -6], [6, 7, -8]), 4),
        (([0, -1, -2], [0, -3, -4], [0, -5, -6], [0, -7, -8]), 1),
    ],
)
def test_sun_of_four(
    value: (List[int], List[int], List[int], List[int]), expected_result: int
):
    actual_result = check_sum_of_four(*value)

    assert actual_result == expected_result
