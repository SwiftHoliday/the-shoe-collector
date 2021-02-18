from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    release = models.CharField(max_length=250)
    price = models.IntegerField()