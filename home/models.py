from django.db import models
from django.contrib import messages


# Create your models here.
class Authenticate(models.Model):
    ACCESS_LEVEL = (
        ('', '------------'),
        ('Admin', 'Admin'),
        ('Supervisor', 'Supervisor'),
        ('Student', 'Student'),
    )

    username = models.CharField(default=None, max_length=100)
    firstname = models.CharField(default=None, max_length=100)
    lastname = models.CharField(default=None, max_length=100)
    access_level = models.CharField(blank=True, null=True, default=None, max_length=100, choices = ACCESS_LEVEL)

    def __str__(self):
       return self.username