"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def iterator(item):
    del_next = False
    for it in reversed(item):
        if it == "#":
            del_next = True
        elif not del_next:
            yield it
        else:
            del_next = False


def backspace_compare(first: str, second: str):
    for f, s in zip_longest(iterator(first), iterator(second)):
        if f != s:
            return False
    return True
