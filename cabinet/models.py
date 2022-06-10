from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from students.models import Student
from supervisors.models import Supervisor
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
        ('proposal', 'Proposal'),
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

    STATUS = (
        ('', '------------'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),  
    )

    # student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    cabinet = models.CharField(blank=True , default='no' ,max_length=100 , choices = FUNCTIONS)
    dapartment = models.CharField(blank=True , default='no' ,max_length=100 , choices = DEPARTMENT)
    document_type = models.CharField(blank=True , default='no' ,max_length=100 , choices = DOCUMENT_TYPE)
    document_title = models.CharField(default="", max_length=30)
    document = models.FileField(upload_to=create_unique_path ,validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','jpg','png' ,'jpeg','doc','xlsx'])])
    notes = models.CharField(blank=True ,null =True , default="" ,max_length=100)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, default=None)    
    reviewer_notes = models.CharField(blank=True ,null =True , default="" ,max_length=100)
    status = models.CharField(blank=True , default='no' ,max_length=100 , choices = STATUS)
    user_name = models.CharField(default=None, max_length=100)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.CharField(default=None, max_length=30)

class ProposalCabinet(models.Model):
    def create_unique_path(instance, filename):
        return os.path.join("uploads/proposal_ideas/"+"/", filename)

    DEPARTMENT = (
        ('', '------------'),
        ('information_systems', 'Information Systems'),
        ('computer_science', 'Computer Science'),
        ('business_studies_and_computing_science', 'Business Studies And Computing Science'),
        ('accounting', 'Accounting'),
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
    document_title = models.CharField(default="", max_length=30)
    cabinet = models.CharField(blank=True , default='no' ,max_length=100 , choices = FUNCTIONS)
    dapartment = models.CharField(blank=True , default='no' ,max_length=100 , choices = DEPARTMENT)
    document = models.FileField(upload_to=create_unique_path ,validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','jpg','png' ,'jpeg','doc','xlsx'])])
    notes = models.CharField(blank=True ,null =True , default="" ,max_length=100)  
    user_name = models.CharField(default=None, max_length=100)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.CharField(default=None, max_length=30)


