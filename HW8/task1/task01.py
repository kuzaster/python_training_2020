"""
We have a file that works as key-value storage,
each like is represented as key and value separated by = symbol, example:
name=kek last_name=top song_name=shadilay power=9001
Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001
In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line 1=something)
ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    def __init__(self, file_path):
        with open(file_path) as data:
            self.data_dict = {}
            for item in data.readlines():
                key, value = map(str.strip, item.split("="))
                try:
                    int(key)
                except ValueError:
                    self.data_dict[key] = value
                    # self.__dict__[key] = value
                else:
                    raise ValueError(f"{item} cannot be assigned to an attribute")

        #     self.data_dict = dict(map(str.strip, item.split('=')) for item in data.readlines())

    def __getattr__(self, key):
        return self.data_dict[key]

    def __getitem__(self, key):
        return self.data_dict[key]
        # return self.__dict__[key]


# storage = KeyValueStorage("/home/tim/PycharmProjects/python_training_2020/HW8/task1/task01.txt")
# print(storage.file_data, type(storage.file_data))
# print(storage.data_dict)
