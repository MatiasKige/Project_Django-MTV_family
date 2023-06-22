from django.shortcuts import render
from app.models import Familiar
from datetime import datetime

# Create your views here.

def agregar_familiar(request):
    new_familiar=Familiar.objects.create(
        name= "Bruno Suarez Murua",
        edad=6,
        parentesco="Sobrino",
        fecha_ingreso=""
    )
    context={
        "new_familiar":new_familiar
    }
    return render(request, "new_familiar.html",context=context)

def mostrar_familiar(request):
    list_familiar=Familiar.objects.all()
    context={
        "list_familiar":list_familiar
    }
    return render(request,"list_familiar.html",context=context)