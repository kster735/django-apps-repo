from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm, ItemDeleteForm

# from datetime import datetime, time, timedelta
# from django.db.models.functions import Now
# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {
        "items_list": items,
    }
    return render(request, 'food/index.html', context)

def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        "id": item.pk,
        "item_name": item.item_name,
        "item_desc": item.item_desc,
        "item_price": item.item_price,
        # "item_created_at": item.item_created_at,
        # "item_last_updated_at": item.item_last_updated_at,
        "item_image": item.item_image,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm(request.GET or None)
    return render(request, 'food/create_item.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        form = ItemForm(request.POST or None, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:detail', id=item.id)
    else:
        form = ItemForm(request.GET or None, instance=item)

    return render(request, 'food/create_item.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(pk=id)
   
    if request.method == 'POST':
        item.delete() 
        return redirect('food:index')
    
    context = {
        "id": item.pk,
        "item_name": item.item_name,
        "item_desc": item.item_desc,
        "item_price": item.item_price,
        # "item_created_at": item.item_created_at,
        # "item_last_updated_at": item.item_last_updated_at,
        "item_image": item.item_image,
    }

    return render(request, 'food/detail.html', context)



