from django.shortcuts import render


def index(request):
    a = 'Text'
    return render(request, 'index.html', context={'name': a})


