from board import Board
from disk import Disk
from game_controller import GameController

# ------------------------------------------------------------------------------------
# IMPORTANT: Because within my add_disk() method, there is a display()
# function, pytest will not run properly. The reason display() is in there
# is because I wanted to implement the delay time for the computer. Commenting
# out the display() function will allow pytest to work, and  all the methods
# will still function as usual with the expected outputs.
# ------------------------------------------------------------------------------------


def test_constructor():
    # Test to see if a board and with different size and height will work
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    assert bd.row == 4
    assert bd.column == 4
    # Middle 4 spots will already contain disk objects on initialization
    # Assert this is correct
    for y in range(len(bd.table)):
        for x in range(len(bd.table)):
            assert bd.table[1][1] and bd.table[1][2] and bd.table[2][1] and \
                bd.table[2][2] != 0
    # Assert other attributes are correct upon initialization
    assert bd.color_flag
    assert bd.gc == gc
    assert not bd.no_more_valid_moves


def test_check_all_positions():
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    # Tests case where board is filled by all black
    # manually insert a white disk at point table[0][0]
    # game ends and method returns expected tuple
    for y in range(len(bd.table)):
        for x in range(len(bd.table)):
            bd.table[y][x] = Disk(y, x, 0)
    bd.table[0][0] = Disk(0, 0, 255)
    assert bd.check_all_positions() == (15, 1)

    # Tests case where board is not filled but
    # there are no more possible valid moves for
    # both sides and game ends. Test returns expected tuple
    gc1 = GameController(400, 400)
    bd1 = Board(4, 4, gc1)
    bd1.table[1][1] = 0
    bd1.table[1][2] = 0
    bd1.table[2][1] = 0
    bd1.table[2][2] = 0
    bd1.table[0][0] = Disk(0, 0, 0)
    bd1.table[0][1] = Disk(0, 1, 255)
    bd1.makevalidmove(250, 0)
    assert bd1.check_all_positions() == (3, 0)


def test_isvalid():
    # Test to make sure isvalid() method functions
    # properly - returns the expected set with the valid
    # moves for the color at that turn
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    assert bd.isvalid() == {(0, 1), (1, 0), (2, 3), (3, 2)}

    gc1 = GameController(400, 400)
    bd1 = Board(4, 4, gc1)
    bd1.table[0][1] = Disk(0, 1, 0)
    bd1.table[1][1] = Disk(1, 1, 0)
    bd1.color_flag = False
    assert bd1.isvalid() == {(0, 0), (2, 0), (0, 2)}


def test_makevalidmove():
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    # Actual coordinates on grid
    # If we try to place a disk object in the table
    # index that already has a disk object, will end function
    # and return None
    assert bd.makevalidmove(100, 100) == None
    # If we try to click on a spot that does not have an object
    # but is not valid, will return empty list, because no tiles
    # were flipped
    assert bd.makevalidmove(50, 50) == []

    # If we successfully add a disk in a spot, color flag
    # will change and it will be the other color's turn, in this
    # case, True flag (Black) switches to False (White)
    gc1 = GameController(400, 400)
    bd1 = Board(4, 4, gc1)
    bd1.table[0][0] = Disk(0, 0, 255)
    bd1.table[0][1] = Disk(0, 1, 255)
    bd1.table[0][2] = Disk(0, 2, 255)
    bd1.table[1][0] = Disk(1, 0, 255)
    bd1.table[1][1] = Disk(1, 1, 255)
    bd1.table[1][2] = Disk(1, 2, 0)
    bd1.table[2][0] = Disk(2, 0, 255)
    bd1.table[2][1] = Disk(2, 1, 0)
    bd1.table[2][2] = Disk(2, 2, 0)
    assert bd1.color_flag
    bd1.makevalidmove(350, 350)
    assert not bd1.color_flag


def test_add_disk():
    # Successfully adding a disk changes the color_flag
    gc = GameController(400, 400)
    bd = Board(4, 4, gc)
    assert bd.color_flag
    bd.makevalidmove(120, 50)
    assert not bd.color_flag

    # Trying to add a disk in the table where there is already
    # a Disk object will return None and will not change the flag
    gc1 = GameController(400, 400)
    bd1 = Board(4, 4, gc1)
    assert bd1.color_flag
    assert bd1.add_disk(1, 1) == None
    assert bd1.color_flag
    bd1.add_disk(0, 1)
    assert not bd1.color_flag
