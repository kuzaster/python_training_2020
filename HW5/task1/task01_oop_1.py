"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """
    Class Homework takes two attributes 'text' - with text of homework
    and 'days' - the amount of days for homework
    Class Homework has such attributes:
        'text' - stores the text of homework
        'deadline' - stores datetime.timedelta object with amount of days for homework
        'created' - stores exact date and time of creation homework
    Class Homework has method 'is_active',
    which check deadline of homework is passed or not. Return boolean
    >>> homework = Homework('Learn functions', 0)
    >>> homework.text
    'Learn functions'
    >>> isinstance(homework.created, datetime.datetime)
    True
    >>> homework.deadline.days
    0
    >>> homework.is_active()
    False
    """

    def __init__(self, text, days):
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self):
        date_now = datetime.datetime.now()
        if self.deadline >= (date_now - self.created):
            return True
        return False


class Student:
    """
    Class Student takes and stores two attributes:
    'last_name' - with the last name of student
    'first_name' - with the first name of student
    Class Student has method 'do_homework',
    which takes class Homework object as argument
    anf return this object if deadline of homework is not passed
    or print 'You are late' and return None otherwise
    >>> student = Student('Roman', 'Petrov')
    >>> student.first_name  # Petrov
    'Petrov'
    >>> homework1 = Homework('Learn functions', 0)
    >>> student.do_homework(homework1)
    You are late
    >>> homework2 = Homework('create 2 simple classes', 5)
    >>> isinstance(student.do_homework(homework2), Homework)
    True
    """

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """
    Class Teacher takes and stores two attributes:
    'last_name' - with the last name of teacher
    'first_name' - with the first name of teacher
    Class Teacher hs method 'create_homework',
    which takes two arguments, 'text' - text of homework
    and 'days' - the amount of days for homework
    and return the instance of class Homework with attributes 'text' and 'days'
    >>> teacher = Teacher('Daniil', 'Shadrin')
    >>> teacher.last_name
    'Daniil'
    >>> homework = teacher.create_homework('Learn functions', 0)
    >>> isinstance(homework, Homework)
    True
    >>> homework.text
    'Learn functions'
    >>> create_homework_too = teacher.create_homework
    >>> homework2 = create_homework_too('create 2 simple classes', 5)
    >>> isinstance(homework2, Homework)
    True
    >>> homework2.text
    'create 2 simple classes'
    """

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, days):
        return Homework(text, days)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # teacher = Teacher('Daniil', 'Shadrin')
    # student = Student('Roman', 'Petrov')
    # teacher.last_name  # Daniil
    # student.first_name  # Petrov
    #
    # expired_homework = teacher.create_homework('Learn functions', 0)
    # expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    # expired_homework.deadline  # 0:00:00
    # expired_homework.text  # 'Learn functions'
    #
    # # create function from method and use it
    # create_homework_too = teacher.create_homework
    # oop_homework = create_homework_too('create 2 simple classes', 5)
    # oop_homework.deadline  # 5 days, 0:00:00
    #
    # student.do_homework(oop_homework)
    # student.do_homework(expired_homework)  # You are late
# teacher = Teacher('Daniil', 'Shadrin')
# student = Student('Roman', 'Petrov')
# print(teacher.last_name)  # Daniil
# print(student.first_name)  # Petrov
#
# expired_homework = teacher.create_homework('Learn functions', 0)
# print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
# print(expired_homework.deadline)  # 0:00:00
# print(expired_homework.text)  # 'Learn functions'
# # print(expired_homework.is_active())
#
# # create function from method and use it
# create_homework_too = teacher.create_homework
# oop_homework = create_homework_too('create 2 simple classes', 5)
# print(oop_homework.deadline)  # 5 days, 0:00:00
# #
#
# student.do_homework(oop_homework)
# student.do_homework(expired_homework)  # You are late
