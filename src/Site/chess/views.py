from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import *


def index(request):
    Game.create_new("John", "Jane")
    game = get_object_or_404(Game, id=1)
    boardsquares = BoardSquare.objects.filter(board=game.board)
    p1_pieces = game.player_one.pieces.all()
    p2_pieces = game.player_two.pieces.all()
    context = {"boardsquares": boardsquares,
               "p1_pieces": p1_pieces,
               "p2_pieces": p2_pieces,
               "current_turn": game.current_turn}
    return render(request, 'chess/chessboard.html', context)

