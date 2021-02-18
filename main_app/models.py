from django.db import models
from django.urls import reverse
# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    release = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})
