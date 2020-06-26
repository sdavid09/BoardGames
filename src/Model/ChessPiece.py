class ChessPiece:
    def __init__(self, name, value, image):
        self.name = name
        self.value = value
        self.image = image

    def __repr__(self):
        return self.name