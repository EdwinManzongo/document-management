from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Student(models.Model):
   
    DEPARTMENT = (
        ('', '------------'),
        ('information_systems', 'Information Systems'),
        ('computer_science', 'Computer Science'),
        ('business_studies_and_computing_science', 'Business Studies And Computing Science'),
        ('accounting', 'Accounting'),
    )

    STUDENT_TYPE = (
        ('', '------------'),
        ('undergraduate', 'Undergraduate'),
        ('postgraduate_masters', 'Post Graduate - Masters'),
        ('postgraduate_doctorate', 'Post Graduate - Doctorate'),
        ('postgraduate_professor', 'Post Graduate - Professor'),
    )

    student_id = models.CharField(default=None, max_length=100)
    fullname = models.CharField(default=None, max_length=100)
    address = models.CharField(default=None, max_length=100)
    contact_number = models.CharField(default=None, max_length=100)
    department = models.CharField(max_length=100 , choices = DEPARTMENT)
    student_type = models.CharField(max_length=100 , choices = STUDENT_TYPE)
    national_id_no = models.CharField(blank=True , null=True, default=None, max_length=100)
    dob = models.CharField(default=None, max_length=100)
    user_id = models.CharField(default=None, max_length=10)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.CharField(default=None, max_length=100)

    def __str__(self):
        return '%s' % "Student Type : "+ self.student_type +" | name: "+ self.fullname