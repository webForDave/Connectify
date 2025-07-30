from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "bio")
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500",
                "placeholder": "Enter your email"
            }),
            "username": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500",
                "placeholder": "Choose a username"
            }),
            "bio": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500",
                "rows": 3,
                "placeholder": "Tell us about yourself..."
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Style password1
        self.fields['password1'].widget.attrs.update({
            "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
            "placeholder": "Create password"
        })

        # Style password2
        self.fields['password2'].widget.attrs.update({
            "class": "w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-indigo-500",
            "placeholder": "Confirm password"
        })

class StyledLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Email Address'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Password'
        })

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "bio")