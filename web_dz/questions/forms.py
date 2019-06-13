from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class MyRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput)
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput)

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def save(self):
        u = User(username=self.username, email=self.email, password=self.password1)
        u.save()
        Profile(user=u)
        Profile.save()