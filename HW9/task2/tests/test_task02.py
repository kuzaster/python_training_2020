from task02 import Suppressor, suppressor


def test_context_manager_as_class_suppresses_exception():
    with Suppressor(IndexError):
        assert [0][1]
    with Suppressor(ValueError):
        assert int("string")


def test_context_manager_as_generator_suppresses_exception():
    with suppressor(IndexError):
        assert [0][1]
    with suppressor(ValueError):
        assert int("string")
