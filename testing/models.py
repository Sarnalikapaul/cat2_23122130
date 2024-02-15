from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserReg(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    addr=models.CharField(max_length=200)
    email=models.CharField(max_length=200)


