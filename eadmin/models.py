from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 30)
    brand = models.CharField(max_length = 20)
    rate = models.FloatField()
    image = models.ImageField(upload_to = 'product/')

