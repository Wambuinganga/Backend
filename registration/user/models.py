from django.db import models


class Account(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
# Create your models here.
