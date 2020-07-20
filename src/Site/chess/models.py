from django.db import models


class Piece(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Board(models.Model):
    rows = 8
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    pieces = models.ManyToManyField(Piece)

    @staticmethod
    def create_new():
        board = Board()
        board.save()
        for row in range(1, board.rows + 1):
            for column in board.columns:
                square = BoardSquare(
                    board=board,
                    row=row,
                    column=column
                )
                square.save()
        return board

class BoardSquare(models.Model):
    board = models.ForeignKey(Board, related_name="board", on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, related_name="piece", on_delete=models.CASCADE,
                                null=True)
    row = models.IntegerField()
    column = models.CharField(max_length=1)

class Player(models.Model):
    name = models.CharField(max_length=30)
    pieces = models.ManyToManyField(Piece)

    def __str__(self):
        return self.name

class Game(models.Model):
    player_one = models.ForeignKey(Player, related_name="player_one", on_delete=models.CASCADE)
    player_two = models.ForeignKey(Player, related_name="player_two", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name="gameboard", on_delete=models.CASCADE)
    current_turn = models.ForeignKey(Player, related_name="current_turn", on_delete=models.CASCADE, default=None)

    @staticmethod
    def create_player_one_pieces():
        pieces = [
            Piece(name='Rook', icon=u'\u2656', color='white'),
            Piece(name='Knight', icon=u'\u2658', color='white'),
            Piece(name='Bishop', icon=u'\u2657', color='white'),
            Piece(name='Queen', icon=u'\u2655', color='white'),
            Piece(name='King', icon=u'\u2654', color='white'),
            Piece(name='Bishop', icon=u'\u2657', color='white'),
            Piece(name='Knight', icon=u'\u2658', color='white'),
            Piece(name='Rook', icon=u'\u2656', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
            Piece(name='Pawn', icon= u'\u2659', color='white'),
        ]
        return pieces

    @staticmethod
    def create_player_two_pieces():
        pieces = [
            Piece(name='Rook', icon=u'\u265C', color='black'),
            Piece(name='Knight', icon=u'\u265E', color='black'),
            Piece(name='Bishop', icon=u'\u265D', color='black'),
            Piece(name='Queen', icon=u'\u265B', color='black'),
            Piece(name='King', icon=u'\u265A', color='black'),
            Piece(name='Bishop', icon=u'\u265D', color='black'),
            Piece(name='Knight', icon=u'\u265E', color='black'),
            Piece(name='Rook', icon=u'\u265C', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
            Piece(name='Pawn', icon= u'\u265F', color='black'),
    ]
        return pieces

    @staticmethod
    def create_new(player_one_name, player_two_name):
        board = Board.create_new()
        player_one_pieces = Game.create_player_one_pieces()
        player1 = Player(
            name=player_one_name,
        )
        player1.save()

        for piece in player_one_pieces:
            piece.save()
            player1.pieces.add(piece)
            board.pieces.add(piece)

        player_two_pieces = Game.create_player_two_pieces()
        player2 = Player(
            name=player_two_name,
        )
        player2.save()
        for piece in player_two_pieces:
            piece.save()
            player2.pieces.add(piece)
            board.pieces.add(piece)

        game = Game(
            player_one = player1,
            player_two = player2,
            board = board,
            current_turn = player1
        )
        game.save()

        first_player_board_pieces = [BoardSquare.objects.filter(board=board.id, row=row, column=col)
                            for col in Board.columns for row in [1,2]]
        # add pieces to board piece
        for row, piece in list(zip(first_player_board_pieces, player_one_pieces)):
            row.update(piece=piece)

        second_player_board_pieces = [BoardSquare.objects.filter(board=board.id, row=row, column=col)
                            for col in Board.columns for row in [8,7]]
        for row, piece in list(zip(second_player_board_pieces, player_two_pieces)):
            row.update(piece=piece)


