import pytest
from task01 import instances_counter


def test_decorator_create_two_new_methods_for_class():
    @instances_counter
    class User:
        pass

    assert hasattr(User, "get_created_instances") is True
    assert hasattr(User, "reset_instances_counter") is True


def test_method_get_created_instances_count_created_instance():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0
    user_1 = User()
    assert user_1.get_created_instances() == 1
    user_2 = User()
    assert user_2.get_created_instances() == 2


def test_method_reset_instances_counter_return_amount_of_created_instances():
    @instances_counter
    class User:
        pass

    user_1, user_2 = User(), User()
    assert user_1.get_created_instances() == 2
    assert user_1.reset_instances_counter() == 2


def test_method_reset_instances_counter_reset_amount_of_created_instances():
    @instances_counter
    class User:
        pass

    user_1, user_2 = User(), User()
    assert user_1.get_created_instances() == 2
    user_1.reset_instances_counter()
    assert user_1.get_created_instances() == 0
