from typing import Callable, List

import pytest
from task03 import Filter


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            (
                [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)],
                range(10),
            ),
            [2, 4, 6, 8],
        ),
        (
            (
                [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)],
                range(-4, 4),
            ),
            [2],
        ),
    ],
)
def test_filtering_even_positive(
    value: (List[Callable], any), expected_result: List[int]
):
    actual_result = Filter(value[0]).apply(value[1])

    assert actual_result == expected_result
