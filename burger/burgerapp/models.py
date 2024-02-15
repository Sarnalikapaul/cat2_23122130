from django.db import models

# Create your models here.
# models.py

class Task(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    task = models.CharField(max_length=100)




