import os
from typing import List

import pytest
from task01 import get_longest_diverse_words


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            os.path.join(os.path.dirname(__file__), "data.txt"),
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "Selbstverständlich",
                "Fingerabdrucks",
                "Friedensabstimmung",
                "außenpolitisch",
                "Seinsverdichtungen",
            ],
        ),
        (
            os.path.join(os.path.dirname(__file__), "data1.txt"),
            [
                "vorgebahnte",
                "Betrachtung",
                "ausführen",
                "verbirgt",
                "vielmehr",
                "bedenkli",
                "Waldgang",
                "hinter",
                "Ausflug",
                "gefaßt",
            ],
        ),
    ],
)
def test_longest_diverse_words(value: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(value)

    assert actual_result == expected_result
