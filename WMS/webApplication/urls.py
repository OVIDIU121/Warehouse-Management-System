from django.urls import path, include
from . import views
# Routes the user through the application
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("pricing", views.pricing_view, name="pricing"),
    path('signup/', views.signup_view, name='signup'),
    path('addInventory/', views.addInventory, name='addInventory'),
]
