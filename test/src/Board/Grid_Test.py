import unittest

from src.Board.Board import Grid

class GridTest(unittest.TestCase):
    def test_grid_size_8x8(self):
        X_SIZE = 8
        Y_SIZE = 8
        grid = Grid(X_SIZE, Y_SIZE)
        self.assertEqual(len(grid), X_SIZE * Y_SIZE)

    def test_grid_size_7x5(self):
        X_SIZE = 7
        Y_SIZE = 5
        grid = Grid(X_SIZE, Y_SIZE)
        self.assertEqual(len(grid), X_SIZE * Y_SIZE)