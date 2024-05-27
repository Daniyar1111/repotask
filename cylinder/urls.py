from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_cylinder, name='calculate_cylinder'),
]
