import pytest
from task03 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"name": "Bill", "last_name": "Gilbert"}, [sample_data[0]]),
        ({"name": "Bill", "type": "bird"}, []),
    ],
)
def test_make_filter(value, expected_result):
    actual_result = make_filter(**value).apply(sample_data)

    assert actual_result == expected_result
