from django.shortcuts import render
from .models import Familiar


def familia(request):
    
    mabel = Familiar(nombre="Mabel", edad=28, fecha_de_nacimiento="1993-12-12")
    alberto = Familiar(nombre="Alberto", edad=72, fecha_de_nacimiento="1950-17-3")
    abigail = Familiar(nombre="Abigail", edad=22, fecha_de_nacimiento="1993-11-2")
    mi_familia = {'familiares': [mabel, alberto, abigail]}
    return render(request, 'familiares1.html', mi_familia)