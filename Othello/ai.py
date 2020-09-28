import random as rand
from board import Board
import time


class Ai:
    """The Ai"""
    def __init__(self, board):  # Takes in board object
        self.board = board

    def computer_move(self, legal_moves_set):
        # Legal moves set is the set returned from board.isvalid()
        """Helps to computer select and make a move"""
        # If color_flag is False and game is not over, Com's turn
        if not self.board.color_flag and \
                not (self.board.gc.black_wins or self.board.gc.white_wins
                     or self.board.gc.tie) and self.board.isvalid():
            print("Computer's Turn")
            if legal_moves_set:
                print("Thinking...")
                time.sleep(0.6)
                tup = rand.choice(tuple(legal_moves_set))
                y, x = tup
                # have to multiply by 100 because makevalidmove
                # takes in floor division in order to get table index
                # so we have to take that into account, as the tuples in
                # the set returned from board.isvalid() method will
                # already be table indexes
                self.board.makevalidmove(x * 100, y * 100)
