from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import *


# def index(request):
#     setup_pieces()
#     game = get_object_or_404(Game, pk=1)
#     context = {'x_header': 'A B C D E F G H'.split(" "),
#                'y_header': list(range(8, 0, -1)),
#                'game': game,
#                'pieces': game.board.pieces.all()}
#     return render(request, 'chess/index.html')

def index(request):
    Game.create_new("Joe", "Sue")
    return render(request, 'chess/chessboard.html')

