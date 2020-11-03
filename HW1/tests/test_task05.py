from typing import List

import pytest

from HW1.tasks.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), 16),
        (([-1, -3, 1, -3, -5, -3, -6, -7], 3), 1),
        (([1, 3, -1, -3, 5, 3, 6, 7], 1), 7),
        (([1, 3, 5, 7], 4), 16),
    ],
)
def test_max_subar_sum(value: (List[int], int), expected_result: int):
    actual_result = find_maximal_subarray_sum(*value)

    assert actual_result == expected_result
