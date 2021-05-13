from django.shortcuts import render
from types import SimpleNamespace
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def home(request):
    return render(request, "pages/home.dj")


def login(request):
    context = {"login_failed": False, "email": "", "password": ""}

    if request.method == "POST":
        email = request.POST.get("auth_email")
        password = request.POST.get("auth_password")
        context["email"] = email
        context["password"] = password

        try:
            user = User.objects.get(email=email)
            if not check_password(password, user.password):
                context["login_failed"] = True
                context["login_error"] = "Password is incorrect"
                login(request, user)

        except User.DoesNotExist:
            context["login_failed"] = True
            context["login_error"] = "No account exist with given email"

    return render(request, "pages/login.dj", context=context)


def signup(request):
    return render(request, "pages/signup.dj")
