from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Use your custom user model
        fields = ("username", "email", "identification", "country", "city", "password1", "password2")  # Adjust fields as needed
