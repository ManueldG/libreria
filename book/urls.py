
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('articoli/<int:id>',views.articoli,name='articoli')
    
]