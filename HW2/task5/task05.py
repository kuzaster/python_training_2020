"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List


def custom_range(seq, *args) -> List[any]:
    sl = slice(*args)
    if sl.start:
        start = seq.index(sl.start)
    else:
        start = 0
    stop, step = seq.index(sl.stop), sl.step or 1
    new_seq = seq[start:stop:step]
    return list(new_seq)


# print(custom_range(string.ascii_lowercase, 'p', 'g', -2))
# print(custom_range(string.ascii_lowercase, 'g', 'p'))
# print(custom_range(string.ascii_lowercase, 'g'))
# print(custom_range([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4, 9, 2))
