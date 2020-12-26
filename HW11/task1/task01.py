class SimplifiedEnum(type):
    def __new__(cls, name, bases, dct):
        key = f"_{name}__keys"
        for item in dct[key]:
            dct[item] = item
        return super().__new__(cls, name, bases, dct)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
