from django.http import HttpResponse
from django.shortcuts import render

#def hello(request):
#    return HttpResponse("Hello,World!")


def runoob(request):
    context = {}
    context['hello'] = 'Hello my friend'
    return render(request, 'runoob.html', context)
