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
    Class Homework has method 'is_active',
    which check deadline of homework is passed or not. Return boolean
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
    Class Student has method 'do_homework',
    which takes class Homework object as argument
    and return this object if deadline of homework is not passed
    or print 'You are late' and return None otherwise
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
    Class Teacher hs method 'create_homework',
    which takes two arguments, 'text' - text of homework
    and 'days' - the amount of days for homework
    and return the instance of class Homework with attributes 'text' and 'days'
    """

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, days):
        return Homework(text, days)
