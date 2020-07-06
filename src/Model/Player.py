
class Player:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.pieces = []

    def __repr__(self):
        return self.name
