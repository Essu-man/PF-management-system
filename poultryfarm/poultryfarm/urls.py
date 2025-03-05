from django.contrib import admin
from django.urls import path
from farm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard.html'),
    path('Inventory/', views.Inventory, name='Inventory.html'),
    path('feed/', views.birds, name='feed.html'),
    path('health/', views.birds, name='health.html'),
    path('reports/', views.birds, name='reports.html'),
    path('birds/', views.birds, name='birds.html'),
    path('', views.dashboard, name='home'),
]
