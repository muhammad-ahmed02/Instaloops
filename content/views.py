from django.shortcuts import render


def home(request):
    return render(request, "pages/home.dj")


def login(request):
    return render(request, "pages/login.dj")


def signup(request):
    return render(request, "pages/signup.dj")
