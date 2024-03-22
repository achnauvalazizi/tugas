from django.urls import path 
from .Views import index

urlpatterns = [
    path ('index', index, name= 'index')
]
