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
from timeit import timeit


def backspace_compare(first: str, second: str):
    f_list, s_list = [], []
    for f, s in zip_longest(first, second):
        if f != "#":
            f_list += f if f else ""
        else:
            if f_list:
                f_list.pop()
        if s != "#":
            s_list += s if s else ""
        else:
            if s_list:
                s_list.pop()
    return f_list == s_list


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("a##c", "#a#c"))
print(backspace_compare("a#c", "b"))

# new_first = "".join(iterator(first))
# new_second = "".join(iterator(second))
# print(new_first, new_second)
# return new_first == new_second
