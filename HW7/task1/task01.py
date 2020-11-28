"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from itertools import chain
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    tree = chain.from_iterable(tree.items())
    occurs = {element: 0}

    def counter(listed_tree, elem):
        for item in listed_tree:
            if isinstance(item, (int, str, bool)):
                if item is elem:
                    occurs[item] += 1
            elif not isinstance(item, dict):
                counter(item, elem)
            else:
                new_item = chain.from_iterable(item.items())
                counter(new_item, element)

    counter(tree, element)
    return occurs[element]


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
