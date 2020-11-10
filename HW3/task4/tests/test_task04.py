import pytest
from task04 import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (153, True),
        (10, False),
        (9, True),
    ],
)
def test_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)

    assert actual_result == expected_result
