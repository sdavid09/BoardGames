from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import *


def setup_pieces():

    rook = Piece(name='Rook', icon=u'\u265C', color='black')
    knight = Piece(name='Knight', icon=u'\u265A', color='black')
    bishop = Piece(name='Knight', icon=u'\u2657', color='black')
    rook.save()
    knight.save()
    bishop.save()

    player1 = Player(name="Joe", pieces=rook)
    player2 = Player(name="Sue", pieces=bishop)
    player1.save()
    player2.save()

def index(request):
    setup_pieces()
    person = get_object_or_404(Player, pk=1)
    print(person)
    context = {'x_header': 'A B C D E F G H'.split(" "), 
               'y_header': list(range(8, 0, -1)),
               'person': person}
    return render(request, 'chess/index.html', context)
