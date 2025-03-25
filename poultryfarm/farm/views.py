
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
    context = {
        'egg_count': 1250,
        'feed_count': 5000,
        'medication_count': 18,
        'equipment_count': 35,
        'inventory_items': InventoryItem.objects.all()
    }
    return render(request, 'inventory.html', context)

def birds(request):
    return render(request, 'birds.html')

def feed(request):
    return render(request, 'feed.html')

def health(request):
    return render(request, 'health.html')

def reports(request):
    return render(request, 'reports.html')