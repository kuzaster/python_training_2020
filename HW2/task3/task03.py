"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    all_comb_lists = []

    def combine(in_lists, cur_comb_list):
        last = len(in_lists) == 1
        n = len(in_lists[0])
        for i in range(n):
            item = cur_comb_list + [(in_lists[0][i])]
            if last:
                all_comb_lists.append(item)
            else:
                combine(in_lists[1:], item)

    combine(args, [])
    return all_comb_lists
