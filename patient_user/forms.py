from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Patient


class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = Patient
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_numer = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass
