import unittest

from src.Board.Grid import Grid

class GridTest(unittest.TestCase):
    def test_grid_size_10x10(self):
        X_SIZE = 10
        Y_SIZE = 10
        grid = Grid(X_SIZE, Y_SIZE)
        self.assertEqual(len(grid), X_SIZE * Y_SIZE)

    def test_grid_size_7x5(self):
        X_SIZE = 7
        Y_SIZE = 5
        grid = Grid(X_SIZE, Y_SIZE)
        self.assertEqual(len(grid), X_SIZE * Y_SIZE)

    def test_get_item(self):
        # get value from 2d array
        grid = Grid(8, 8, "*")
        self.assertEqual(grid[0][0], "*")

    def test_get_entire_row(self):
        # get entire row of grid
        grid = Grid(8, 8, "*")
        self.assertEqual(grid[0], ["*","*", "*", "*", "*", "*", "*", "*"])

    def test_set_item(self):
        # assign value to a 2d array
        grid = Grid(8, 8)
        grid[0][0] = 9
        self.assertEqual(grid[0][0], 9)

    def test_set_entire_row(self):
        # get entire row of grid
        grid = Grid(8, 8, "*")
        grid[0]= ["X","X", "*", "*", "X", "X", "X", "*"]
        self.assertEqual(grid[0], ["X","X", "*", "*", "X", "X", "X", "*"])

    def test_get_entire_board(self):
        # get entire row of grid
        grid = Grid(3, 3, "*")
        self.assertEqual(str(grid), "[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]")


