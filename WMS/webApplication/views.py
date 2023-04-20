from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "webApplication/index.html")
    return render(request, "webApplication/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user  is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "webApplication/login.html", {
                "message": "Invalid credentials, check your login information !"
            })
    return render(request, "webApplication/login.html")

def logout_view(request):
    logout(request)
    return render(request, "webApplication/login.html", {
        "message": "Logged out."
    })