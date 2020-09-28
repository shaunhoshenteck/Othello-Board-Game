class Score:
    """Records Score"""
    def __init__(self, file):
        self.file = file
        self.list_name_score = []
        self.read_file(file)
        self.score_flag = True

    def read_file(self, file):
        """Reads file and appends contents to a list
        as a tuple if text file contains name and score
        """
        try:
            with open(file, 'r') as f:
                for line in f:
                    temp = line.split()
                    if temp:
                        x, y = temp
                        self.list_name_score.append((x, int(y)))
        except FileNotFoundError:
            print('Unable to find', file)

    def score_to_list(self, name, black_score):
        """ Compares scores within self.list_name_score and either
        appends or inserts at index 0 based on score"""
        # Need a flag because this method is called under draw because it is
        # in gc. So when a name and score is successful inserted into the list
        # and written, score_flag will become False.
        if self.score_flag and name != '':  # Makes sure name is entered
            # Only enters this if statement if the text file isn't empty,
            # which means if it is the second player onwards
            if self.list_name_score:
                x, y = self.list_name_score[0]
                if black_score >= y:
                    self.list_name_score.insert(0, (name, black_score))
                else:
                    self.list_name_score.append((name, black_score))
            # if text file is empty, that means self.list_name_score will
            # be empty, so append name and score directly to list
            else:
                self.list_name_score.append((name, black_score))

    def list_to_file(self):
        """Iterates through list self.list_name_score and writes
        name and score to file on every line as string"""
        if self.score_flag:
            with open('scores.txt', 'w') as f:
                for x, y in self.list_name_score:
                    f.write(str(x) + " " + str(y) + "\n")
            self.score_flag = False
