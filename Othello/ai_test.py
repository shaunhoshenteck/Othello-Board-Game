from board import Board
from game_controller import GameController
from ai import Ai


def test_constructor():
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    test = Ai(bd)
    assert test.board == bd


def test_computer_move():
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    test = Ai(bd)
    test.computer_move(test.board.isvalid())
    assert test.board.color_flag

    gc1 = GameController(400, 400)
    bd1 = Board(4, 4, gc)
    test1 = Ai(bd)
    not test1.board.color_flag
    test1.computer_move(test.board.isvalid())
    assert test1.board.color_flag
