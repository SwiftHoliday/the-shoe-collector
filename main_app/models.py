from django.db import models
from django.urls import reverse
from datetime import date

CLEANERS = (
    ('R', 'Reshoevn8r'),
    ('SL', 'Sneaker Lab'),
    ('JM', 'Jason Markk'),
)
# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sellers_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
    name = models.CharField(max_length=75)
    brand = models.CharField(max_length=75)
    release = models.CharField(max_length=75)
    price = models.IntegerField()
    sellers = models.ManyToManyField(Seller)


    def cleaned_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(CLEANERS)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    cleaner = models.CharField(
        max_length=2,
        choices=CLEANERS,
        default=CLEANERS[0][0]
    )

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cleaning with {self.get_cleaner_display()} at {self.date}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for shoe id #{self.shoe_id} @ {self.url}"

class Meta:
    ordering = ['-date']


