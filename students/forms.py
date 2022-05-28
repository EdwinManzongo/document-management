from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from students.models import Student

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        
        fields = ['fullname', 'address','contact_number', 'national_id_no', 'dob', 'student_type', 'department']

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
            'national_id_no': forms.TextInput(attrs={
                "class":"form-control signin-email",
            }),
            'dob': DatePickerInput(attrs={
                "class":"form-control signin-email",
            }),
            # 'dob': forms.TextInput(attrs={
            #     "class":"form-control signin-email",
            # }),
            'student_type': forms.Select(attrs={
                "class":"form-control signin-email",
            }),
            'department': forms.Select(attrs={
                "class":"form-control signin-email",
            }),
        }

