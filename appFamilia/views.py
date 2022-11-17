from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

def familia(request):
    mabel = Familiar(nombre="Mabel", edad=28, fecha_de_nacimiento=1993-12-12)
    mabel.save()
    cadena = "Familiar guardado: " + mabel
    return HttpResponse(cadena)