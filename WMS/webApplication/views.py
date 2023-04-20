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
    return render(request, "webApplication/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
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


def receive_items(item_id, location_id, preadvice_id, received_qty):
    item = get_object_or_404(Item, pk=item_id)
    location = get_object_or_404(Location, pk=location_id)
    preadvice = get_object_or_404(PreAdvice, pk=preadvice_id)
    try:
        with transaction.atomic():
            # Check if there is a pre-advice line for the item
            preadvice_item = preadvice.items.filter(item=item).first()
            if not preadvice_item:
                raise ValueError(
                    f"No pre-advice line found for item {item.name}")

            # Update the pre-advice item's received quantity
            preadvice_item.received_qty += received_qty

            # Check if the received quantity matches the expected quantity
            if preadvice_item.received_qty == preadvice_item.expected_qty:
                preadvice_item.status = 'Received'
                preadvice.save()

            # If the received quantity is less than the expected quantity, update the pre-advice item's status
            elif preadvice_item.received_qty < preadvice_item.expected_qty:
                preadvice_item.status = 'Partially received'
                preadvice.save()

            # If the received quantity is greater than the expected quantity, raise an error
            else:
                raise ValueError(
                    "Received quantity cannot be greater than expected quantity")

            # Create an inventory item for the received item in the specified location
            inventory_item, created = Inventory.objects.get_or_create(
                item=item,
                location=location,
                defaults={'quantity': 0},
            )
            inventory_item.quantity += received_qty
            inventory_item.save()

    except ValueError as e:
        return str(e)

    return "Received items successfully"
