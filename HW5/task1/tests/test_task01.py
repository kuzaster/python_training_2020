from task01 import Homework, Student, Teacher


def test_method_is_true_of_class_Homework_with_expired_homework():
    expired_homework = Homework("some text", 0)

    assert not expired_homework.is_active()


def test_method_is_true_of_class_Homework_with_actual_homework():
    actual_homework = Homework("some another text", 5)

    assert actual_homework.is_active()


def test_method_do_homework_of_class_Student_with_expired_homework(capfd):
    student = Student("Roman", "Petrov")
    expired_homework = Homework("some text", 0)
    student.do_homework(expired_homework)
    out, err = capfd.readouterr()

    assert student.do_homework(expired_homework) is None
    assert out == "You are late\n"


def test_method_do_homework_of_class_Student_with_actual_homework():
    student = Student("Roman", "Petrov")
    actual_homework = Homework("some another text", 5)

    assert isinstance(student.do_homework(actual_homework), Homework)


def test_method_create_homework_of_class_Teacher():
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("Learn functions", 0)
    isinstance(homework, Homework)

    assert isinstance(homework, Homework)
    assert homework.text == "Learn functions"
