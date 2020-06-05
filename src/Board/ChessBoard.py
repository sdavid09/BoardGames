from .Grid import Grid

whitepieces = {
    'WKing'   : u'\u2654',
    'WQueen'  : u'\u2655',
    'WRook'   : u'\u2656',
    'WBishop' : u'\u2657',
    'WKnight' : u'\u2658',
    'WPawn'   : u'\u2659',
}

blackpieces = {
    'BKing'   : u'\u265A',
    'BQueen'  : u'\u265B',
    'BRook'   : u'\u265C',
    'BBishop' : u'\u265D',
    'BKnight' : u'\u265E',
    'BPawn'   : u'\u265F',
}

class ChessBoard:
    def __init__(self):
        self.board = Grid(8,8)

    def __len__(self):
        return len(self.board)

    def __repr__(self):
        return repr(self.board)

