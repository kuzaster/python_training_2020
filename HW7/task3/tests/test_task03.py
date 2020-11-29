from task03 import tic_tac_toe_checker


def test_tic_tac_toe_checker_with_winner_line():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_tic_tac_toe_checker_with_winner_column():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_tic_tac_toe_checker_with_winner_diagonals():
    board = [["x", "-", "o"], ["-", "x", "o"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_tic_tac_toe_checker_with_draw():
    board = [["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "draw!"


def test_tic_tac_toe_checker_with_unfinished():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "unfinished!"
