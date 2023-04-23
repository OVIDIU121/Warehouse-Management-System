from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


# Redirects user to home page or view inventory page
def index(request):
    if not request.user.is_authenticated:
        return render(request, "webApplication/index.html")
    return render(request, "webApplication/viewInventory.html")


# Login view, checks if user is can log in and returns relevant page
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "webApplication/viewInventory.html")
        else:
            return render(request, "webApplication/login.html", {
                "message": "Invalid credentials, check your login information !"
            })
    return render(request, "webApplication/login.html")


# Display a logout page.
def logout_view(request):
    logout(request)
    return render(request, "webApplication/login.html", {
        "message": "Logged out."
    })


# View for a pricing page.
def pricing_view(request):
    return render(request, "webApplication/pricing.html")


# Sign up a user.
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
            return render(request, "webApplication/viewInventory.html")
    else:
        form = SignUpForm()
    return render(request, 'webApplication/signup.html', {'form': form})


# Render a form to add an inventory to web application.
def addInventory(request):
    return render(request, "webApplication/addInventory.html")
