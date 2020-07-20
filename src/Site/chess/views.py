from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import *


def index(request):
    Game.create_new("John", "Jane")
    return render(request, 'chess/chessboard.html')

