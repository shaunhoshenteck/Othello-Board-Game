from game_controller import GameController
from score import Score


def test_constructor():
    gc = GameController(400, 400)
    assert gc.WIDTH == 400
    assert gc.HEIGHT == 400
    assert not gc.black_wins
    assert not gc.white_wins
    assert not gc.tie
    assert gc.scores


def test_save_name():
    gc = GameController(400, 400)
    gc.save_name('tester')
    assert gc.name == 'tester'
