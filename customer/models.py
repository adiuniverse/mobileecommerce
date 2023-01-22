from django.db import models
from common.models import Customer
from eadmin.models import Product
# Create your models here.


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE )
    product = models.ForeignKey(Product, on_delete = models.CASCADE )