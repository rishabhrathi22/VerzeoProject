from django.db import models

# Create your models here.

class Student(models.Model):
    Sid = models.IntegerField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)