from .Grid import Grid


class ChessBoard:
    row = {'A': 0, 'B': 1, 'C': 2,'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7}
    col = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1, 8:0}

    def __init__(self):
        self.board = Grid(8, 8, "*")

    def __setitem__(self, position, value):
        row, col = self.check_chess_notation(position)
        if row and col:
            self.board[self.col[int(col)]][self.row[row.upper()]] = value
        else:
            self.board[position] = value

    def __getitem__(self, position):
        row, col = self.check_chess_notation(position)
        if row and col:
            return self.board[self.col[int(col)]][self.row[row.upper()]]
        else:
            return self.board[position]

    @staticmethod
    def check_chess_notation(position):
        """ Check if first character is letter, Second is number and  """
        row, col = '', ''
        if ( len(str(position)) == 2 and position[0].isalpha()
                                   and int(position[1]) >= 1
                                   and int(position[1]) <= 8 ):
            row, col = position
        return row, col

    @classmethod
    def convert_to_chess_notation(cls, position):
        row, col = position
        for letter, num in cls.row.items():
            if num == row:
                row = letter
                break

        for num, num_map in cls.col.items():
            if num_map == col:
                col = num
                break

        return row, col

    def __len__(self):
        return len(self.board)

    def __repr__(self):
        top_bar = ''.join([' '] * 2 + ['{:^2}'.format(item) for item in sorted(self.row.keys())])
        board = []
        board +=  [''.join(['{:2}'.format(item) for item in row ]) for row in self.board]
        board_with_numbers = []
        count = 8
        for row in board:
            board_with_numbers.append("".join(['{:2}{:2}{}'.format(str(count), ''.join(list(row)), str(count))]))
            count-=1

        row = "\n".join(board_with_numbers)
        return  "\n" + top_bar + "\n" + row + "\n" + top_bar





