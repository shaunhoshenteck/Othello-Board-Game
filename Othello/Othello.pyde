from board import Board
from game_controller import GameController
from ai import Ai

WIDTH = 800
PIXEL_BOX_LENGTH = 100
LINES_NEEDED = WIDTH / PIXEL_BOX_LENGTH

gc = GameController(WIDTH, WIDTH)
# GameController object will be part of this Board object, this is so we can determine
# the winner, the loser, or the tie
main_game = Board(8, 8, gc) 
ai = Ai(main_game)

def setup():
    size(WIDTH, WIDTH)
    colorMode(RGB)
    stroke(0, 0, 0)
    strokeWeight(3)
    name = input('Enter your name')
    gc.save_name(name)
    
      
def draw():
    background(0, 105, 0)
    for x in range(LINES_NEEDED - 1):
        line(x * 100 + 100, 0, x * 100 + 100, WIDTH) # Vertical lines drawn
        line(0, x * 100 + 100, WIDTH, x * 100 + 100)  # Horizontal lines drawn
    main_game.display()
    ai.computer_move(main_game.isvalid())
    total_black, total_white = main_game.check_all_positions() # Tuple unpacking
    gc.update(total_black, total_white)
    
def mousePressed():
    # Adds a disk to the board based on add_disk() method with mouseX and mouseY as parameters
    # main_game.add_disk(mouseX, mouseY)
    main_game.makevalidmove(mouseX, mouseY)
    
def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)  
