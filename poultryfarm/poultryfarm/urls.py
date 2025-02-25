from django.contrib import admin
from django.urls import path
from farm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', views.inventory_dashboard, name='inventory_dashboard.html'),
    path('', views.inventory_dashboard, name='home'),
]