from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=30)
    fatherName = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    msg = models.TextField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.name