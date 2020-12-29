from task02 import backspace_compare


def test_backspace_compare_with_equal_string():
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")
    assert backspace_compare("ca#c#", "c")
    assert backspace_compare("xabd###c", "xc")


def test_backspace_compare_with_unequal_string():
    assert not backspace_compare("a#c", "#ac")
    assert not backspace_compare("a#c", "c#")
    assert not backspace_compare("ca#c", "c")
