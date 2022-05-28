from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from students.models import Student
from django.utils import timezone
from django.core.validators import FileExtensionValidator
import os

# Create your models here.
class Cabinet(models.Model):
    def create_unique_path(instance, filename):
        return os.path.join("uploads/"+str(instance.cabinet)+"/client"+"/", filename)

    DEPARTMENT = (
        ('', '------------'),
        ('information_systems', 'Information Systems'),
        ('computer_science', 'Computer Science'),
        ('business_studies_and_computing_science', 'Business Studies And Computing Science'),
        ('accounting', 'Accounting'),
    )

    DOCUMENT_TYPE = (
        ('', '------------'),
        ('chapter_1', 'Chapter 1'),
        ('chapter_2', 'Chapter 2'),
        ('chapter_3', 'Chapter 3'),
        ('chapter_4', 'Chapter 4'), 
        ('chapter_5', 'Chapter 5'),
        ('chapter_6', 'Chapter 6'),
        ('chapter_7', 'Chapter 7'), 
        ('final_document', 'Final Document'),
    )

    FUNCTIONS = (
        ('', '------------'),
        ('undergraduate_dissertation', 'Undergraduate Dissertation'),
        ('masters_thesis', 'Masters Thesis'),
        ('phd_thesis', 'PHD Thesis'),
        ('professor_thesis', 'Professor Thesis'),
        ('research', 'Research'),  
    )

    # student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    cabinet = models.CharField(blank=True , default='no' ,max_length=100 , choices = FUNCTIONS)
    dapartment = models.CharField(blank=True , default='no' ,max_length=100 , choices = DEPARTMENT)
    document_type = models.CharField(blank=True , default='no' ,max_length=100 , choices = DOCUMENT_TYPE)
    document_title = models.CharField(default="", max_length=30)
    document = models.FileField(upload_to=create_unique_path ,validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','jpg','png' ,'jpeg','doc','xlsx'])])
    notes = models.CharField(blank=True ,null =True , default="" ,max_length=100)
    user_name = models.CharField(default=None, max_length=100)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.CharField(default=None, max_length=30)


# class Cabinet(models.Model):
   
#     DEPARTMENT = (
#         ('', '------------'),
#         ('corporate', 'Corporate'),
#         ('individual', 'Individual'),
#     )

#     fullname_or_company_name = models.CharField(default=None, max_length=100)
#     address = models.CharField(default=None, max_length=100)
#     contact_number = models.IntegerField(default=None)
#     client_type = models.CharField(blank=True , default='no' ,max_length=100 , choices = DEPARTMENT)
#     national_id_no_or_company_reg_number = models.CharField(default=None, max_length=100)
#     occupation_or_main_line_of_business= models.CharField(default=None, max_length=100)
#     dob_or_date_of_incorporation= models.DateField(default=None)
#     # account_type = models.IntegerField(default=None)
#     created_at = models.DateField(default=None)
#     updated_at = models.DateField(default=None)
#     created_by = models.IntegerField(default=None)

#     def __str__(self):
#         return '%s' % self.fullname_or_company_name