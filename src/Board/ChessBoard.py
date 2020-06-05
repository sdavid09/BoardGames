from .Grid import Grid

whitepieces = {
    'King'   : u'\u2654',
    'Queen'  : u'\u2655',
    'Rook'   : u'\u2656',
    'Bishop' : u'\u2657',
    'Knight' : u'\u2658',
    'Pawn'   : u'\u2659',
}

blackpieces = {
    'King'   : u'\u265A',
    'Queen'  : u'\u265B',
    'Rook'   : u'\u265C',
    'Bishop' : u'\u265D',
    'Knight' : u'\u265E',
    'Pawn'   : u'\u265F',
}

class ChessBoard:
    def __init__(self):
        self.board = Grid(8,8)
        self.row ={'A': 1, 'B': 2, 'C': 3,
                   'D': 4, 'E': 5, 'F': 6,
                   'G': 7, 'H': 8}

    def __len__(self):
        return len(self.board)

    def __repr__(self):
        return repr(self.board)

    def __setitem__(self, position, value):
        row, col = self.check_chess_notation(position)
        if row and col:
            self.board[self.row[row.upper()]][int(col)] = value
        else:
            self.board[position] = value

    def __getitem__(self, position):
        row, col = self.check_chess_notation(position)
        if row and col:
            return self.board[self.row[row.upper()]][int(col)]
        else:
            return self.board[position]

    def check_chess_notation(self, position):
        """ Check if first character is letter, Second is  number - 1 and greater then 0 """
        row, col = '', ''
        if len(str(position)) == 2 and position[0].isalpha() \
                                   and int(position[1]) \
                                   and int(position[1]) >= 1 \
                                   and int(position[1]) - 1 >= 0:
            row, col = position
        return row, col


