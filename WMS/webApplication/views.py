from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.shortcuts import get_object_or_404
from django.db import transaction
from api.models import Item, Location, PreAdvice, PreAdviceItem, Inventory

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "webApplication/index.html")
    return render(request, "webApplication/viewInventory.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "webApplication/manage.html")
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


def pricing_view(request):
    return render(request, "webApplication/pricing.html")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST["username"]
            raw_password = request.POST["password1"]
            confirm_password = request.POST["password2"]
            raw_email = request.POST["email"]
            raw_fn = request.POST["first_name"]
            raw_ln = raw_fn = request.POST["first_name"]

            user = authenticate(username=username, password=raw_password, )
            login(request, user)
            return redirect("webApplication/user.html")
    else:
        form = SignUpForm()
    return render(request, 'webApplication/signup.html', {'form': form})


def addInventory(request):
    return render(request, "webApplication/addInventory.html")
