from task01 import SimplifiedEnum


class ColorsEnumWithNoMeta:
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnumWithNoMeta:
    __keys = ("XL", "L", "M", "S", "XS")


class ColorsEnumWithMeta(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnumWithMeta(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_creation_attr_from_keys():
    assert not hasattr(SizesEnumWithNoMeta, "L")
    assert not hasattr(ColorsEnumWithNoMeta, "BLUE")

    assert hasattr(SizesEnumWithMeta, "L")
    assert SizesEnumWithMeta.L == "L"

    assert hasattr(ColorsEnumWithMeta, "BLUE")
    assert ColorsEnumWithMeta.BLUE == "BLUE"
