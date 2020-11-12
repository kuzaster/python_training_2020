from io import StringIO

import pytest
from task01 import cache


@cache(times=1)
def f():
    return input("? ")


first_input = StringIO("first\n")


def test_cache(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", first_input)
        first_out = f()  # First run function f() with input "first"
        second_out = f()  # Remember previous output function f() only one times
        third_out = f()  # Raise error EOFError, because it's waiting new input
        assert first_out == second_out != third_out
