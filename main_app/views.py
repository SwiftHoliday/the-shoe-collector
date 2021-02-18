from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Shoe
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})
    
def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/detail.html', {'shoe': shoe})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'