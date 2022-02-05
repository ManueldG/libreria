from django.shortcuts import render
from .models import Autore, Genere, Articolo


def index(request):
    return render(request,'index.html')
