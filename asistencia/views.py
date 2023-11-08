from django.shortcuts import render, get_object_or_404
from curso.models import Curso
from alumnado.models import Alumno
from django.db.models import F
# Create your views here.

def asistencia(request):
    cursos = Curso.objects.all()
    return render(request, 'asistencia.html', {'cursos':cursos})

def listaAlumnos(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)

    if Alumno.objects.filter(id_curso = id_curso).exists():
        alumnos = Alumno.objects.filter(id_curso = id_curso)
        context = {
            'alumnos':alumnos,
            'curso':curso
        }
        if request.method == 'POST':
            alumnos.filter(id_curso=id_curso).update(cantidad_asistencias = F('cantidad_asistencias') + 1)
            curso.cantidad_clases +=1
            curso.save()
            
        return render(request, 'lista_alumnos.html', context)
    else:
        return render(request, 'no_alumnos.html')
    
