import pytest
from task02 import fast_sum_of_slow_calc


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (500, 60),
    ],
)
def test_fast_sum_of_slow_calc(value: int, expected_result: (int, int)):
    actual_result = fast_sum_of_slow_calc(value)[1]

    assert actual_result <= expected_result
