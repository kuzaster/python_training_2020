from typing import Sequence

import pytest
from tasks.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3], True),
        ([0, 1, 1, 3, 4], False),
        ([0, 1], True),
    ],
)
def test_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
