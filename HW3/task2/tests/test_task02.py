import pytest
from task02 import fast_sum_of_slow_calc


def test_fast_sum_of_slow_calc():
    actual_result = fast_sum_of_slow_calc(500)[1]

    assert actual_result <= 60
