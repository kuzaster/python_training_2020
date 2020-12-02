"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class MyLibraryError(Exception):
    """Base exception in my library"""


class DeadlineError(MyLibraryError):
    """Error for situation when deadline passed"""


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


class HomeworkResult:
    """This class stores Homework, the author(Student) of this homework and solution of this homework"""

    def __init__(self, author, homework, solution):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.solution = solution
        self.created = datetime.datetime.now()


class PersonalData:
    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(PersonalData):
    """
    Class Student has method 'do_homework',
    which takes class Homework object and solution(string) as arguments
    and return this object of class HomeworkResult if deadline of homework is not passed
    or raise DeadlineError with message 'You are late' otherwise
    """

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class Teacher(PersonalData):
    """
    Method 'create_homework' takes two arguments, 'text' - text of homework
    and 'days' - the amount of days for homework
    and return the instance of class Homework with attributes 'text' and 'days'
    Method check_homework takes class object HomeworkResult and check if length of solution more than 5.
    If more, this solution is saved in 'homework_done' and return True, or return False and save nothing otherwise
    Method 'save_homework_result' takes class object HomeworkResult as argument and save original solution of homework.
    Class method 'reset_results' takes class object Homework as optional argument.
    If Homework is given - method delete all saved solutions in 'homework_done' for this Homework.
    If no argument is given, method reset all 'homework_done'
    """

    homework_done = defaultdict(list)

    def create_homework(self, text, days):
        return Homework(text, days)

    def save_homework_result(self, homework_result):
        homework_instance = homework_result.homework
        for saved_homework in self.homework_done[homework_instance]:
            if saved_homework.solution == homework_result.solution:
                return False
        self.homework_done[homework_instance].append(homework_result)

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5:
            self.save_homework_result(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if isinstance(homework, Homework):
            cls.homework_done[homework] = []
        else:
            cls.homework_done = defaultdict(list)


# if __name__ == '__main__':
#     opp_teacher = Teacher('Daniil', 'Shadrin')
#     advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
#
#     lazy_student = Student('Roman', 'Petrov')
#     good_student = Student('Lev', 'Sokolov')
#
#     oop_hw = opp_teacher.create_homework('Learn OOP', 1)
#     docs_hw = opp_teacher.create_homework('Read docs', 5)
#     fail_hw = opp_teacher.create_homework('Read docs', 0)
#
#     result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
#     result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
#     result_3 = lazy_student.do_homework(docs_hw, 'done')
#     try:
#         result_4 = HomeworkResult(good_student, "fff", "Solution")
#     except Exception as err:
#         print(err)
#     opp_teacher.check_homework(result_1)
#     temp_1 = opp_teacher.homework_done
#
#     advanced_python_teacher.check_homework(result_1)
#     temp_2 = Teacher.homework_done
#     assert temp_1 == temp_2
#
#     opp_teacher.check_homework(result_2)
#     opp_teacher.check_homework(result_3)
#
#     print(Teacher.homework_done[oop_hw])
#     Teacher.reset_results()
#     print(Teacher.homework_done[oop_hw])
