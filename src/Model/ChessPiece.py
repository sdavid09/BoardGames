class ChessPiece:
    def __init__(self, name, color, icon):
        self.name = name
        self.color = color
        self.icon = icon

    def __repr__(self):
        return self.name

class Rook(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("Rook", color, icon)

class Knight(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("Knight", color, icon)

class Bishop(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("Bishop", color, icon)

class Queen(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("Queen", color, icon)

class King(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("King", color, icon)

class Pawn(ChessPiece):
    def __init__(self, color, icon=''):
        super().__init__("Pawn", color, icon)