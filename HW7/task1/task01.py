"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from itertools import chain
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    tree = chain.from_iterable(tree.items())
    occurs = {element: 0}

    def counter(listed_tree, elem):
        for item in listed_tree:
            if isinstance(item, (int, str, bool)):
                occurs[elem] += 1 if item is elem else 0
            elif not isinstance(item, dict):
                counter(item, elem)
            else:
                new_item = chain.from_iterable(item.items())
                counter(new_item, element)

    counter(tree, element)
    return occurs[element]
