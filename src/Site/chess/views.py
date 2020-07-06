from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    context = {'board_size': range(64)}
    return render(request, 'chess/index.html', context)
