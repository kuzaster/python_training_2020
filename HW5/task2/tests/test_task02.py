from task02 import new_wrapper, print_result


def test_wrapped_function_not_save_internal_values():
    def function_name(n):
        """Some information about function"""
        return n

    function_name = print_result(function_name)

    assert function_name.__name__ != "function_name"
    assert function_name.__doc__ != "Some information about function"


def test_wrapped_function_save_internal_values():
    def function_name(n):
        """Some information about function"""
        return n

    print_result = new_wrapper(
        function_name
    )  # apply new_wrapper to wrapping function "print_result"
    function_name = print_result(function_name)

    assert function_name.__name__ == "function_name"
    assert function_name.__doc__ == "Some information about function"


def test_wrapped_function_has_no_attribute_original_func():
    def function_name(n):
        """Some information about function"""
        return n

    function_name = print_result(function_name)

    assert not hasattr(function_name, "__original_func")


def test_wrapped_function_has_attribute_original_func():
    def function_name(n):
        """Some information about function"""
        return n

    print_result = new_wrapper(function_name)
    function_name = print_result(function_name)

    assert hasattr(function_name, "__original_func")


def test_wrapped_function_new_attribute_original_func_equal_this_function():
    def function_name(n):
        """Some information about function"""
        return n

    print_result = new_wrapper(function_name)
    function_name = print_result(function_name)

    assert function_name.__original_func == function_name
