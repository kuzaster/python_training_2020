from task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", 1, "of", "RED", 10000000],
    },
    "third": {
        "It": True,
        "jhl": "RED",
        "complex_key": {
            "key1": 1,
            "key2": "RED",
            "key3": ["a", "lot", 1, "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_find_occurrences():
    assert find_occurrences(example_tree, "RED") == 6
    assert find_occurrences(example_tree, 1) == 3
    assert find_occurrences(example_tree, True) == 1
    assert find_occurrences(example_tree, 10000000) == 1
