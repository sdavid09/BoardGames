
class Grid:
    """ Creates a 2D array specified by row and column """

    def __init__(self, X_SIZE, Y_SIZE, item=""):
        self._grid = [[item for x in range(X_SIZE)]
                              for y in range(Y_SIZE)]

    def __len__(self):
        return sum([len(element) for element in self._grid])

    def __getitem__(self, position):
        return self._grid[position]

    def __setitem__(self, index, value):
        self._grid[index] = value

    def __repr__(self):
        return "\n".join([''.join(['{:2}'
                   .format(item) for item in row])
                                    for row in self._grid])
