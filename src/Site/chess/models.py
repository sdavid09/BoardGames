from django.db import models


class Piece(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=30)
    pieces = models.ManyToManyField(Piece)

    def __str__(self):
        return self.name

class Board(models.Model):
    columns = models.IntegerField(default=8)
    rows = models.IntegerField(default=8)
    pieces = models.ManyToManyField(Piece)

    def setup(self):
        pass

class Game(models.Model):
    session = models.CharField(max_length=50)
    player_one = models.ForeignKey(Player, related_name="player_one", on_delete=models.CASCADE)
    player_two = models.ForeignKey(Player, related_name="player_two", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name="board", on_delete=models.CASCADE)
    current_turn = models.ForeignKey(Player, related_name="current_turn", on_delete=models.CASCADE)