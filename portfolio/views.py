from itertools import product
from django.shortcuts import render
from .models import Project # Podemos hacer uso de los modelos de portfolio dentro de las vistas

# Create your views here.

def portfolio(request):
    # return HttpResponse(html_base+"<h2>Este es mi portafolio</h2>")
    projects = Project.objects.all() # Nos devuelve todos los objetos que tiene el modelo de proyecto
    return render(request,"portfolio/portfolio.html",{"projects":projects})
    