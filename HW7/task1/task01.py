"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    occurs = 0

    def counter(values):
        nonlocal occurs
        for item in values:
            if isinstance(item, (int, str, bool)):
                occurs += 1 if item is element else 0
            elif not isinstance(item, dict):
                counter(item)
            else:
                new_values = item.values()
                counter(new_values)

    counter(tree.values())
    return occurs
