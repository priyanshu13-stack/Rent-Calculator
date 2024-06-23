from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_rent, name='calculate_rent'),
    path('reset/', views.reset_last_units, name='reset_last_units'),
]
