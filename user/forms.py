from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import MyUser  # or MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email','username')