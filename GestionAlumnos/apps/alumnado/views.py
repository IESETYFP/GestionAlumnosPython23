from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    return render(request, "index.html")


def home(request):
    alumnos = Alumno.objects.all()

    return render(request, "gestionAlumno.html", {"alumnos": alumnos})

