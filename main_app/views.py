from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Seller
from .forms import CleaningForm
# Create your views here.
class ShoeCreate(CreateView):
    model = Shoe
    fields = ['name', 'brand', 'release', 'price']
    
class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['price', 'release']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})
    
def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    sellers_shoe_doesnt_have = Seller.objects.exclude(id__in=shoe.sellers.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', {
        'shoe': shoe, 'cleaning_form': cleaning_form,
        'seller': sellers_shoe_doesnt_have
    })

def add_cleaning(request, shoe_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = shoe_id
        new_cleaning.save()
    return redirect('shoes_detail', shoe_id=shoe_id)

    
def assoc_seller(request, shoe_id, seller_id):
    Shoe.objects.get(id=shoe_id).sellers.add(seller_id)
    return redirect('shoes_detail', shoe_id=shoe_id)


class SellerList(ListView):
    model = Seller

class SellerDetail(DetailView):
    model = Seller

class SellerCreate(CreateView):
    model = Seller
    fields = '__all__'

class SellerUpdate(UpdateView):
    model = Seller
    fields = ['name']

class SellerDelete(DeleteView):
    model = Seller
    success_url = '/sellers/'  