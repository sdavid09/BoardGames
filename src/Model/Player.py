
class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.pieces = []

    def __repr__(self):
        return self.name
