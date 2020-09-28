class Disk:
    """A Disk"""
    def __init__(self, row, column, color):
        self.color = color
        self.column = column
        self.row = row

    def display(self):
        """Draws the disk based on x and y position"""
        fill(self.color)
        ellipse(self.column * 100 + 50, self.row * 100 + 50, 90, 90)
