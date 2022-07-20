from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Supervisor(models.Model):
   
    DEPARTMENT = (
        ('', '------------'),
        ('information_systems', 'Information Systems'),
        ('computer_science', 'Computer Science'),
        ('business_studies_and_computing_science', 'Business Studies And Computing Science'),
        ('accounting', 'Accounting'),
    )

    supervisor_id = models.CharField(default=None, max_length=100)
    fullname = models.CharField(default=None, max_length=100)
    address = models.CharField(default=None, max_length=100)
    contact_number = models.CharField(default=None, max_length=100)
    department = models.CharField(max_length=100 , choices = DEPARTMENT)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.CharField(default=None, max_length=100)

    def __str__(self):
        return self.supervisor_id