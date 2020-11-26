import sys
from unittest.mock import MagicMock

import pytest
from task02 import DeadlineError, Homework, HomeworkResult, Student, Teacher

student_1 = Student("Roman", "Petrov")
student_2 = Student("Lev", "Sokolov")
teacher = Teacher("Daniil", "Shadrin")
actual_homework = Homework("Some text", 5)
expired_homework = Homework("Another text", 0)


def test_raising_error_when_homework_is_not_instance_Homework():
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(student_1, "not instance of Homework", "Solution")


def test_method_do_homework_return_result_of_work_when_deadline_is_on():
    assert isinstance(
        student_1.do_homework(actual_homework, "Some solution"), HomeworkResult
    )


def test_method_do_homework_raising_error_when_deadline_is_off():
    with pytest.raises(DeadlineError, match="You are late"):
        student_1.do_homework(expired_homework, "Some solution")


def test_method_check_homework_with_right_solution(monkeypatch):
    monkeypatch.setattr(Teacher, "save_homework_result", MagicMock())
    result = student_1.do_homework(actual_homework, "More than 5 symbols")
    assert teacher.check_homework(result) is True


def test_method_check_homework_with_wrong_solution():
    result = student_1.do_homework(actual_homework, "Less")
    assert teacher.check_homework(result) is False


def test_method_check_homework_save_right_solution():
    result = student_1.do_homework(actual_homework, "More than 5 symbols too")
    teacher.check_homework(result)
    assert result.homework in teacher.homework_done.keys()


def test_method_check_homework_not_save_the_same_solution():
    new_homework = Homework("New text", 3)
    result_1 = student_1.do_homework(new_homework, "The same solution")
    result_2 = student_2.do_homework(new_homework, "The same solution")
    assert len(teacher.homework_done[new_homework]) == 0
    teacher.check_homework(result_1)
    assert len(teacher.homework_done[new_homework]) == 1
    teacher.check_homework(result_2)
    assert len(teacher.homework_done[new_homework]) == 1


def test_method_reset_results_delete_result_of_getting_homework():
    assert len(teacher.homework_done[actual_homework]) == 1
    teacher.reset_results(actual_homework)
    assert len(teacher.homework_done[actual_homework]) == 0


def test_method_reset_results_without_parameter_delete_all_results_in_homework_done():
    assert len(teacher.homework_done) == 2
    teacher.reset_results()
    assert len(teacher.homework_done) == 0
