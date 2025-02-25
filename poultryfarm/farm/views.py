
from django.shortcuts import render

from .models import InventoryItem


def inventory_dashboard(request):
    items = InventoryItem.objects.all()
    low_stock_items = [item for item in items if item.is_low_stock()]
    return render(request, 'inventory_dashboard.html', {
        'items': items,
        'low_stock_items': low_stock_items
    })

def orders(request):
    return render(request, 'orders.html')

def settings(request):
    return render(request, 'settings.html')