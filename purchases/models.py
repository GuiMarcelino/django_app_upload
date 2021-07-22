
from os import name
from django.db import models

# Create your models here.
class Purchaser(models.Model):
    name = models.CharField(max_length=255)



class Item(models.Model):
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Merchant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Purchase(models.Model):
    count = models.IntegerField()
    purchaser = models.ForeignKey(Purchaser, on_delete=models.SET_NULL, null= True)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null= True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)