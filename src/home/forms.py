from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from home.models import Authenticate

class AuthenticateForm(forms.ModelForm):
    class Meta:
        model = Authenticate

        fields = ['username','firstname','lastname','access_level']

        widgets  = {
            'username': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'firstname': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'lastname': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'access_level': forms.Select(attrs={
                "class":"form-control",
            }),
        }