from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from students.models import Student
from cabinet.models import Cabinet

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

class DocumentCreateForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        # print(data['client'].client_type)
        # if data['client'].client_type != data['client_type'] :
        #     msg = data['client'].client_type+' account type should match Client type section'
        #     self.add_error('client_type', msg)

    class Meta:
        model = Cabinet

        # 'department',
        fields = ['cabinet', 'document_type', 'document_title', 'document', 'notes', 'supervisor']

        widgets  = {
            'cabinet': forms.Select(attrs={
                "class":"form-control custom-select",
                # "disabled":True,
                "required":True,
            }),
            'document_type': forms.Select(attrs={
                "class":"form-control",
            }),
            'document_title': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'document': forms.ClearableFileInput(
                attrs={
                    "type" : "file",
                    "class":"form-control"
                }
            ),
            'department': forms.TextInput(attrs={
                "class":"form-control",
                "id":"contact_number"
            }),         
            'notes': forms.TextInput(attrs={
                "class":"form-control",
                "rows":3
            }),
            'supervisor': forms.Select(attrs={
                "class":" form-control custom-select",
            }),
        }


class DocumentEditForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
       
        # if data['client'].client_type != data['client_type'] :
        #     msg = data['client'].client_type+' account type should match Client type section'
        #     self.add_error('client_type', msg)
    class Meta:

        model = Cabinet
 

        fields = ['document_type', 'document_title', 'document', 'notes', 'supervisor']

        widgets  = {
            
            'function': forms.Select(attrs={
                "class":" form-control custom-select",
            }),
            'client': forms.Select(attrs={
                "class":"js-example-basic-single form-control custom-select",
            }),
            'cabinet': forms.Select(attrs={
                # "class":"js-example-basic-single form-control custom-select",
                "class":"form-control custom-select",
                "disabled":True,
                "required":True,
            }),
            'client_type': forms.Select(attrs={
                "class":"form-control",
            }),
            'document_type': forms.Select(attrs={
                "class":"form-control",
            }),
            'document_title': forms.TextInput(attrs={
                "class":"form-control",
            }),
            'document': forms.ClearableFileInput(
                attrs={
                    "type" : "file",
                    "class":"form-control"
                }
            ),
            'department': forms.TextInput(attrs={
                "class":"form-control",
                "id":"contact_number"
            }),
            'notes': forms.TextInput(attrs={
                "class":"form-control",
                "rows":3
            }),
            'supervisor': forms.Select(attrs={
                "class":" form-control custom-select",
            }),
        }


class DocumentReviewForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
       
        # if data['client'].client_type != data['client_type'] :
        #     msg = data['client'].client_type+' account type should match Client type section'
        #     self.add_error('client_type', msg)
    class Meta:

        model = Cabinet
 
        # , 'supervisor', 'reviewer_notes'
        fields = ['document_type', 'document_title', 'document', 'notes', 'supervisor', 'reviewer_notes']

        widgets  = {
            
            'function': forms.Select(attrs={
                "class":" form-control custom-select",
             
            }),
            'client': forms.Select(attrs={
                "class":"js-example-basic-single form-control custom-select",
             
            }),
            'cabinet': forms.Select(attrs={
                # "class":"js-example-basic-single form-control custom-select",
                "class":"form-control custom-select",
                "disabled":True,
                "required":True,
             
            }),
            'client_type': forms.Select(attrs={
                "class":"form-control",
             
            }),
            'document_type': forms.Select(attrs={
                "class":"form-control",
            }),
            'document_title': forms.TextInput(attrs={
                "class":"form-control",
             
            }),
            'document': forms.ClearableFileInput(
                attrs={
                    "type" : "file",
                    "class":"form-control"
                }
            ),
            'department': forms.TextInput(attrs={
                "class":"form-control",
                "id":"contact_number"
            }),
            'notes': forms.TextInput(attrs={
                "class":"form-control",
                "rows":3
            }),
            'supervisor': forms.Select(attrs={
                "class":"form-control",
            }),
            'reviewer_notes': forms.TextInput(attrs={
                "class":"form-control",
                "rows":3
            }),
        }
