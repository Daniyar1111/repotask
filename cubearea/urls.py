from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate_area, name='calculate_area'),
]