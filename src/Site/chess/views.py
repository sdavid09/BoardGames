from django.http import HttpResponse

from django.shortcuts import render

def index(request):

    context = {'x_header': 'A B C D E F G H'.split(" "), 
               'y_header': list(range(8, 0, -1))}
    return render(request, 'chess/index.html', context)
