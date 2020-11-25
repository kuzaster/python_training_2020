"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""

    class Icounter(cls):
        created_instances = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.created_instances += 1

        @classmethod
        def get_created_instances(cls):
            return cls.created_instances

        @classmethod
        def reset_instances_counter(cls):
            try:
                return cls.created_instances
            finally:
                cls.created_instances = 0

    return Icounter


# @instances_counter
# class User:
#     pass
#
#
# if __name__ == '__main__':
#
#     print(User.get_created_instances())  # 0
#     user, _, _ = User(), User(), User()
#     print(user.get_created_instances())  # 3
#     print(user.reset_instances_counter())  # 3
