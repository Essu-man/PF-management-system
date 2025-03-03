
from django.shortcuts import render

from .models import InventoryItem


def dashboard(request):
    items = InventoryItem.objects.all()
    low_stock_items = [item for item in items if item.is_low_stock()]
    return render(request, 'dashboard.html', {
        'items': items,
        'low_stock_items': low_stock_items
    })

def Inventory(request):
    return render(request, 'Inventory.html')

def birds(request):
    return render(request, 'birds.html')