from score import Score


class GameController:
    """Maintains the state of the game."""

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.black_wins = False
        self.white_wins = False
        self.tie = False
        self.scores = Score('scores.txt')

    def save_name(self, name):
        """Saves a name"""
        self.name = name

    def update(self, black, white):
        """Carries out necessary actions if black or white wins"""
        if self.black_wins:
            fill(200, 200, 0)
            textSize(80)
            text("BLACK WINS" + "\nBLACK: " + str(black) + "\nWHITE: " +
                 str(white), self.WIDTH/2 - 150, self.HEIGHT/2 - 50)
            self.scores.score_to_list(self.name, black)
            self.scores.list_to_file()

        if self.white_wins:
            fill(200, 200, 0)
            textSize(50)
            text("WHITE WINS" + "\nBLACK: " + str(black) + "\nWHITE: " +
                 str(white), self.WIDTH/2 - 150, self.HEIGHT/2 - 50)
            self.scores.score_to_list(self.name, black)
            self.scores.list_to_file()

        if self.tie:
            fill(200, 200, 0)
            textSize(50)
            text("TIE!" + "\nBLACK: " + str(black) + "\nWHITE: " +
                 str(white), self.WIDTH/2 - 150, self.HEIGHT/2 - 50)
            self.scores.score_to_list(self.name, black)
            self.scores.list_to_file()
