from django.urls import path
from . import views

urlpatterns = [
   path('sport/', views.sport, name='sport'),
   path('action/', views.action, name='action'),
   path('scary/', views.scary, name='scary'),
]
