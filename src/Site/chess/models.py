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
    pieces = models.ManyToManyField(Piece)

class Game(models.Model):
    session = models.CharField(max_length=50, primary_key=True)
    player_one = models.ForeignKey(Player, related_name="player_one", on_delete=models.CASCADE)
    player_two = models.ForeignKey(Player, related_name="player_two", on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)