import pytest
from task04 import is_armstrong


@pytest.mark.parametrize(
    "value",
    [
        9,
        153,
        370,
    ],
)
def test_is_armstrong(value: int):
    assert is_armstrong(value) is True


@pytest.mark.parametrize(
    "value",
    [
        10,
        125,
        256,
    ],
)
def test_is_not_armstrong(value: int):
    assert is_armstrong(value) is False
