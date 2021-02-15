from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('clear', views.clear),
    path('update_guess', views.update_guess),
    path('new_number', views.generate_number)
]
