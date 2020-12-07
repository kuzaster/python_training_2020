from task02 import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_method_len():
    assert len(presidents) == 3


def test_in_method():
    assert "Yeltsin" in presidents
    assert "Kim Kim" not in presidents


def test_access_by_key():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert presidents["Trump"] == ("Trump", 1337, "US")


def test_for_loops():
    presidents_names = ["Yeltsin", "Trump", "Big Man Tyrone"]
    presidents_ages = [999, 1337, 101]
    index = -1
    for president in presidents:
        index += 1
        assert president["name"] == presidents_names[index]
        assert president["age"] == presidents_ages[index]
