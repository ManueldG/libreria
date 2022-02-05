from django.shortcuts import render
from .models import Autore, Genere, Articolo


def index(request):
    art = Articolo.objects.all()
    context = {'art' : art}
    return render(request,'index.html',context)

def articoli(request,id):

    art = Articolo.objects.get(id=id)
    aut = Autore.objects.get(id = art.autore.id)
    

    context = {'id':id,'art':art,'aut':aut}

    return render(request,'articoli.html',context)
