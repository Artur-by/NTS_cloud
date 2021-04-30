from django.db import models

# Create your models here.

class Users(models.Model):
    unp = models.IntegerField(max_length=9)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



