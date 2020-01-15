from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "navbar.html")


def login(request):
    return render(request, "login.html")