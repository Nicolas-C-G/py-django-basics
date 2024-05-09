from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader

# Create your views here.

def home(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an item</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html',context);

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:home')
    
    return render(request,'food/item-form.html',{'form':form})

