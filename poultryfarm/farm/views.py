from django.http import HttpResponse
from django.shortcuts import render

from .models import InventoryItem


def home(request):
    return HttpResponse("Welcome to the Poultry Farm Management System!")

def inventory_dashboard(request):
    items = InventoryItem.objects.all()
    low_stock_items = [item for item in items if item.is_low_stock()]
    return render(request, 'inventory_dashboard.html', {
        'items': items,
        'low_stock_items': low_stock_items
    })