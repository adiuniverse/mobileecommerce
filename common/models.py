from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 30)
    contact = models.BigIntegerField()
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 20)
    confirm = models.CharField(max_length = 20)




class Eadmin(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)