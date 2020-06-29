class ChessPiece:
    def __init__(self, name, player, color, icon):
        self.name = name
        self.player = player
        self.color = color
        self.icon = icon

    def __repr__(self):
        return self.name

class Rook(ChessPiece):
    def __init__(self, player, color, icon):
        super().__init__("Rook", player, color, icon)

    def __repr__(self):
        return self.name