from disk import Disk


class Board:
    """ A Board"""

    def __init__(self, row, column, gc):
        self.row = row
        self.column = column
        # list comprehension for a nested list with all 0s
        self.table = [[0] * self.column for i in range(self.row)]
        # Have to create 4 disk objects in the center when game starts
        self.table[int(self.row/2) - 1][int(self.column / 2) - 1] = \
            Disk(self.row / 2 - 1, self.column / 2 - 1, 255)
        self.table[int(self.row/2) - 1][int(self.column / 2)] = \
            Disk(self.row / 2 - 1, self.column / 2, 0)
        self.table[int(self.row/2)][int(self.column / 2) - 1] = \
            Disk(self.row/2, self.column / 2 - 1, 0)
        self.table[int(self.row/2)][int(self.column / 2)] = \
            Disk(self.row/2, self.column / 2, 255)
        self.color_flag = True
        self.gc = gc
        self.no_more_valid_moves = False
        # Prints the first 'Player's Turn' on to the terminal
        print("Player's Turn")

    def check_all_positions(self):
        """Checks the board to see if all positions are filled"""

        count = 0
        black_count = 0
        white_count = 0
        # For every position on the board, if it is filled
        # by a disk object, add 1 to count
        for i in range(self.row):
            for j in range(self.column):
                if self.table[i][j]:
                    count += 1

        # This means all positions are filled
        if count == (self.row * self.column):
            for i in range(self.row):
                for j in range(self.column):
                    if self.table[i][j].color == 0:
                        black_count += 1
                    if self.table[i][j].color == 255:
                        white_count += 1

            if black_count > white_count:
                self.gc.black_wins = True

            if white_count > black_count:
                self.gc.white_wins = True

            if white_count == black_count:
                self.gc.tie = True

        # Even though the board is not filled, there are no more valid
        # moves, hence the game will end - Tally counts of black and white
        elif count != (self.row * self.column) and self.no_more_valid_moves:
            for i in range(self.row):
                for j in range(self.column):
                    if self.table[i][j] and self.table[i][j].color == 0:
                        black_count += 1
                    if self.table[i][j] and self.table[i][j].color == 255:
                        white_count += 1

            if black_count > white_count:
                self.gc.black_wins = True

            if white_count > black_count:
                self.gc.white_wins = True

            if white_count == black_count:
                self.gc.tie = True

        return black_count, white_count

    def add_disk(self, table_index_y, table_index_x):
        """Method to add a black or white disk to the board, checks if
        position that we want to add in already has a disk"""

        # If element in the linked list is already an object, end function
        if self.table[table_index_y][table_index_x]:
            return

        # Determines what color to put down based on flag.
        # Always starts with black, which is when color_flag is True
        if self.color_flag:
            self.table[table_index_y][table_index_x] = \
                Disk(table_index_y, table_index_x, 0)
            # Self Display method mentioned in pytest comments
            # For pytest to work, comment out self.display()
            # Functions will still work as normal, just without delay
            self.display()
            self.color_flag = False  # After put down disk, make flag False

        # If color_flag is False, means white disk is going to be put down
        elif not self.color_flag:
            self.table[table_index_y][table_index_x] = \
                Disk(table_index_y, table_index_x, 255)
            self.color_flag = True  # After put down disk, make flag True

        # The method isvalid() is called with this method - isvalid()
        # isvalid() checks all the valid moves at that turn for a specific
        # color and returns a set of tuples, which are (row, column) indexes
        # for that color

        self.isvalid()

        # If the first isvalid() check returns an empty set, which
        # is False, we change the color_flag to the opposite color and
        # print the statements accordingly.
        if not self.isvalid():
            if self.color_flag:
                self.color_flag = False
                print("No more moves for player. Computer's turn")

            elif not self.color_flag:
                self.color_flag = True
                print("No more moves for computer. Player's turn")

        # We check one more time after the color_flag has changed
        self.isvalid()

        # If the set is empty once again, it will empty this if statement
        if not self.isvalid():
            self.no_more_valid_moves = True
            print("No more valid moves. Game Over")

    def makevalidmove(self, x, y):
        """Makes a valid move on the board"""

        # Floor division for x and y based on coordinates on the board
        # will give us the indexes of y(row) and x(column) of nested table
        # This is used in line with MousedPressed() function in Processing
        table_index_x = x//100
        table_index_y = y//100

        # If spot is already filled with a disk object, end function
        if self.table[table_index_y][table_index_x]:
            return

        # Conditional for color because being able to put down
        # a disk requires a check based on color
        if self.color_flag:
            color = 0
            other_color = 255
        else:
            color = 255
            other_color = 0

        list_of_tiles_to_flip = []

        # Check for a specific spot starts here
        # 8 directions to check are listed in a list
        # We iterate through this table and check each element one by one
        # If the test fails for say [0, 1], we continue and move on with [1, 0]
        for xdirection, ydirection in [[0, 1], [1, 0], [1, 1], [0, -1],
                                       [-1, 0], [1, -1], [-1, -1], [-1, 1]]:
            # Variable assignment with our x and y indexes after floor division
            x_indicator, y_indicator = table_index_x, table_index_y
            x_indicator += xdirection  # first step in the direction
            y_indicator += ydirection  # first step in the direction

            # If the spot that we are clicking is within the range of the board
            # and in the direction we are checking, there is a disk of the
            # opposite color (if it is black's turn opposite color is white)
            # Then we add the direction to the coordinates
            if (y_indicator in range(self.row)
                and x_indicator in range(self.row)) and \
               self.table[y_indicator][x_indicator] and \
               self.table[y_indicator][x_indicator].color == other_color:
                x_indicator += xdirection
                y_indicator += ydirection

                # Continue checking in that direction, if we come to an empty
                # space with no disk object, it means in this direction there
                # are no tiles we can flip, so we continue and move on with
                # checking the next one (if on [0, 1], we move on to [1, 0])
                if (y_indicator in range(self.row)
                    and x_indicator in range(self.row)) and \
                   not self.table[y_indicator][x_indicator]:
                    continue

                # If we are checking a direction and the opposite color
                # is present, we keep checking that direction
                while (y_indicator in range(self.row) and
                       x_indicator in range(self.row)) and \
                        self.table[y_indicator][x_indicator].color == \
                        other_color:
                    x_indicator += xdirection
                    y_indicator += ydirection

                    # We check in that direction until we check a spot on the
                    # board and we encounter an empty space. Then we
                    # break out of while loop, then continue in for loop
                    if (y_indicator in range(self.row) and
                        x_indicator in range(self.row)) and \
                       not self.table[y_indicator][x_indicator]:
                        break

                # This statements moves on to the next direction to check
                # if we encounter an empty space at the end of the while loop
                if (y_indicator in range(self.row) and
                        x_indicator in range(self.row)) and \
                        not self.table[y_indicator][x_indicator]:
                    continue

                # If we encounter the color we are looking for (opposite color)
                # we go into a while loop where we backtrack to the starting
                # position and we append the indexes we backtracked to a list
                # called list_of_tiles_to_flip
                if (y_indicator in range(self.row) and
                        x_indicator in range(self.row)) and \
                        self.table[y_indicator][x_indicator].color == color:

                    while True:
                        x_indicator -= xdirection
                        y_indicator -= ydirection
                        if x_indicator == table_index_x and \
                           y_indicator == table_index_y:
                            break
                        list_of_tiles_to_flip.append(
                            [y_indicator, x_indicator])

                # This flips the disks using the list
                # list_of_tiles_to_flip
                for y, x in list_of_tiles_to_flip:
                    self.table[y][x] = Disk(y, x, color)

        print("Flipped Tiles:", list_of_tiles_to_flip)
        print("")

        # If list_of_tiles_to_flip is not 0, it means
        # the spot is a valid move, because putting a disk
        # down at that spot will flip disks of the other
        # opposite color, so we go into the method add_disk()
        if len(list_of_tiles_to_flip) != 0:
            self.add_disk(table_index_y, table_index_x)

        # This statment is for a case where it is the
        # player's turn and there are no more moves for
        # the player. The player would click and it would
        # switch to computer's turn
        if self.color_flag and not self.isvalid():
            print("No more moves for player. Computer's turn")
            # If it is player's turn and no more valid moves for player
            # basically where no more tiles are able to be flipped and it
            # doesnt go into add_disk(), switch to
            # computer's turn (color_flag = False)
            self.color_flag = False
            if not self.color_flag and not self.isvalid():
                print("No more valid moves. Game Over.")

        # Print Player's Turn to terminal everytime it is his turn
        if self.color_flag and \
                not (self.gc.black_wins or self.gc.white_wins or self.gc.tie) \
                and self.isvalid():
            print("Player's Turn")

        return list_of_tiles_to_flip

    def isvalid(self):
        """Checks all the valid moves for a specific color during its turn"""
        valid_list = []
        valid_set = set()

        if self.color_flag:
            color = 0
            other_color = 255
        else:
            color = 255
            other_color = 0

        # Based on the color flag parameters, Iterate through all
        # elements in the nested table. If the element does not
        # contain a Disk object, we proceed with the check
        for i in range(self.row):
            for j in range(self.column):
                if self.table[i][j] == 0:
                    for xdirection, ydirection in [[0, 1], [1, 0], [1, 1],
                                                   [0, -1], [-1, 0], [1, -1],
                                                   [-1, -1], [-1, 1]]:
                        x_indicator, y_indicator = j, i
                        # first step in the direction
                        x_indicator += xdirection
                        # first step in the direction
                        y_indicator += ydirection

                        # If it is on the board and when checking a specific
                        # direction, there is a disk of the opposite color,
                        # We keep going in that direction
                        if (y_indicator in range(self.row) and
                                x_indicator in range(self.row)) and \
                                self.table[y_indicator][x_indicator] and \
                                self.table[y_indicator][x_indicator].color == \
                                other_color:
                            x_indicator += xdirection
                            y_indicator += ydirection

                            # If we check in a specific direction and we
                            # encounter an empty spot, we continue with
                            # another direction
                            if (y_indicator in range(self.row) and
                                    x_indicator in range(self.row)) and \
                                    not self.table[y_indicator][x_indicator]:
                                continue

                            # While we encounter disks of the opposite color,
                            # we keep going in that direction until we
                            # encounter an empty spot, then we break
                            while (y_indicator in range(self.row) and
                                   x_indicator in range(self.row)) and \
                                    self.table[y_indicator][x_indicator].color\
                                    == other_color:
                                x_indicator += xdirection
                                y_indicator += ydirection

                                if (y_indicator in range(self.row)
                                    and x_indicator in range(self.row)) \
                                        and not \
                                        self.table[y_indicator][x_indicator]:
                                    break

                            # Once out of while loop check to see if that space
                            # is an empty space, if it is, then we continue
                            if (y_indicator in range(self.row) and
                                    x_indicator in range(self.row)) and \
                                    not self.table[y_indicator][x_indicator]:
                                continue

                            # If we encounter a disk of the correct color,
                            # it means that there are tiles to flip in the
                            # middle of our starting point and this disk
                            # of the same color so we will use these table
                            # indexes and append it to valid_list
                            if (y_indicator in range(self.row) and
                                x_indicator in range(self.row)) and \
                                    self.table[y_indicator][x_indicator].color\
                                    == color:
                                valid_list.append([i, j])

        # Iterate through valid_list list and append the values into a set as
        # tuples this set will be used in add_disk method, especially
        # for the ai
        for x, y in valid_list:
            valid_set.add((x, y))

        # print(valid_set)
        return valid_set

    def display(self):
        """Display starting disks"""
        # table[1][1], [1][2], [2][1], [2][2]
        for i in range(self.row):
            for j in range(self.column):
                # table is all 0s if not filled by an object, means False
                if self.table[i][j]:
                    self.table[i][j].display()
