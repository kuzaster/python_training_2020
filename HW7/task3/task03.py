"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    board = list(chain.from_iterable(board))
    win_combs = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for comb in win_combs:
        f, s, t = comb
        if board[f] == board[s] == board[t] != "-":
            return f"{board[f]} wins!"
    return "draw!" if "-" not in board else "unfinished!"
