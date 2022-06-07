from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.
def familiares(request):
    familiar_1 = Familiares.objects.create(
        nombre = "Gabriela",
        apellido = "Peon",
        edad = 52,
        fecha_nacimiento = "1969-9-11",
        parentesco = "mamá"
    )
    familiar_2 = Familiares.objects.create(
        nombre = "Diego",
        apellido = "Mendoza",
        edad = 27,
        fecha_nacimiento = "1995-3-16",
        parentesco = "novio"
    )
    familiar_3 = Familiares.objects.create(
        nombre = "Franco",
        apellido = "Garcia",
        edad = 23,
        fecha_nacimiento = "1998-1-11",
        parentesco = "hermano"
    )
    
    context = { "familiar_1" : familiar_1,
                "familiar_2" : familiar_2,
                "familiar_3" : familiar_3 }

    return render (request, "template.html", context = context)
        