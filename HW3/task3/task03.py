class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


"""
    The places of bugs are highlighted by <>:
    positive_even = Filter(<lamba> a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance<(int, a)>)
"""


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(dict_val, key=key, value=value):
            return key in dict_val and dict_val[key] == value

        # the defaults function with bugs:
        # def keyword_filter_func(value): -> should be given non-defaults param "dic_val"
        #                                    and defaults parameters "key' and "value"
        # return value[key] == value -> should be added checking availability of "key" in "dic_val"

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
