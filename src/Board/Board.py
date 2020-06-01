
class Board:
    pass

class Grid(Board):
    """ Creates a 2D array specified by row and column """

    def __init__(self, X_SIZE, Y_SIZE):
        self.grid = [[(x, y) for x in range(X_SIZE)] for y in range(Y_SIZE)]

    def __len__(self):
        return sum([len(element) for element in self.grid])
