from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(
        max_length=150,
        required=True,
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "username": "Choose a username",
            "first_name": "Your first name",
            "last_name": "Your last name",
            "email": "you@example.com",
            "password1": "Create a password",
            "password2": "Confirm your password",
        }

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = placeholders.get(name, "")

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = UserProfile
        fields = (
            "phone",
            "address",
            "profile_image",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields["first_name"].initial = self.user.first_name
            self.fields["last_name"].initial = self.user.last_name
            self.fields["email"].initial = self.user.email
            self.fields["phone"].widget.attrs["placeholder"] = "e.g. 01700000000"
            self.fields["address"].widget.attrs["placeholder"] = "Your current address"

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


    def save(self, commit=True):
        profile = super().save(commit=False)

        if self.user:
            self.user.first_name = self.cleaned_data["first_name"]
            self.user.last_name = self.cleaned_data["last_name"]
            self.user.email = self.cleaned_data["email"]
            self.user.save()

        if commit:
            profile.save()

        return profile