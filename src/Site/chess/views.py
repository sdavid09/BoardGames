from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import *

def create_player_one_pieces():
    Piece.objects.bulk_create([
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
    ])

def create_player_two_pieces():
    Piece.objects.bulk_create([
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
    ])
def setup_pieces():
    create_player_one_pieces()
    create_player_two_pieces()

    player1 = Player(name="Joe")
    player2 = Player(name="Sue")
    player1.save()
    player2.save()
    for piece in Piece.objects.all():
        player1.pieces.add(piece)

    myboard = Board()
    myboard.save()
    for piece in Piece.objects.all():
        myboard.pieces.add(piece)
    
    myboard.save()
    game = Game.objects.create(session="abc", player_one=player1, player_two=player2, board=myboard)


def index(request):
    # setup_pieces()
    # game = get_object_or_404(Game, pk=1)
    # context = {'x_header': 'A B C D E F G H'.split(" "), 
    #            'y_header': list(range(8, 0, -1)),
    #            'game': game,
    #            'pieces': game.board.pieces.all()}
    return render(request, 'chess/index.html')


# class DetailView(generic.DetailView):
#     model = Game
#     template_name = 'chess/index.html'

