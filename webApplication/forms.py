from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Creates a signup form for a user.
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name')
