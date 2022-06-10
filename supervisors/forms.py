from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from supervisors.models import Supervisor

class SupervisorCreateForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        
        fields = ['fullname', 'address','contact_number', 'department']

        widgets  = {
            'fullname': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'address': forms.TextInput(attrs={
                "class":"form-control signin-email",
            }),
            'contact_number': forms.TextInput(attrs={
                "class":"form-control signin-email",
            }),
            'department': forms.Select(attrs={
                "class":"form-control signin-email",
            }),
        }

