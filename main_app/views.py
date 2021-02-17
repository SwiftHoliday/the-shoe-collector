from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class Shoe:
    def __init__(self, name, brand, price, release):
        self.name = name
        self.brand = brand
        self.price = price
        self.release = release

shoes = [
    Shoe('Yeezy Boost 350 Zebra', 'Adidas', '$375', '2017-02-25'),
    Shoe('Yeezy Boost 350 Bred', 'Adidas', '$360', '2017-02-11'),
    Shoe('Off-White x Air Max 90', 'Nike', '$530', '2019-02-07'),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes })