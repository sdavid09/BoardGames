
class Grid:
    """ Creates a 2D array specified by row and column """

    def __init__(self, X_SIZE, Y_SIZE):
        self.grid = [["*" for x in range(X_SIZE)] for y in range(Y_SIZE)]

    def __len__(self):
        return sum([len(element) for element in self.grid])

    def __getitem__(self, position):
            return self.grid[position]

    def __repr__(self):
        return str(self.grid)
