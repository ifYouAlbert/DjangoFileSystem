from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def work(request):
    return render(request, 'work.html')
