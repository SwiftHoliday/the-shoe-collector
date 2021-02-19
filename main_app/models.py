from django.db import models
from django.urls import reverse
# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sellers_detail', kwargs={'pk': self.id})



class Shoe(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    release = models.CharField(max_length=250)
    price = models.IntegerField()
    sellers = models.ManyToManyField(Seller)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})
