from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def filter(request):
    return render(request, "filter.html")