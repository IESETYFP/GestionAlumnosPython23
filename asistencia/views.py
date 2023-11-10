from django.shortcuts import render, get_object_or_404
from .models import Asistencia
from curso.models import Curso
from alumnado.models import Alumno
from django.db.models import F

# Create your views here.
def asistencia(request):
    cursos = Curso.objects.all()
    return render(request, 'asistencia.html', {'cursos':cursos})

def listaAlumnos(request, id_curso):
    # Obtener de la clase curso donde coincida el ID
    curso = get_object_or_404(Curso, id_curso=id_curso)
    
    # Obtenemos los alumnos de ese curso específico
    alumnos = Alumno.objects.filter(id_curso = id_curso)

    # A este if se ingresa cuando se aprieta el boton "guardar" en el HTML
    if request.method == 'POST':
        for alumno in alumnos:
            # Obtenemos en que alumnos esta presionado el input checkbox para sumar su asistencia
            checkbox_name=f"asistencia_{alumno.id_alumno}"
            if checkbox_name in request.POST:
                alumno.cantidad_asistencias = F('cantidad_asistencias') +1
                alumno.save()
                # Crear objeto Asistencia relacionado con el alumno
                Asistencia.objects.create(id_alumno=alumno)
        curso.cantidad_clases +=1
        curso.save()

    alumnos = Alumno.objects.filter(id_curso=id_curso)
    for alumno in alumnos:
        alumno.cantidad_inasistencias = curso.cantidad_clases - alumno.cantidad_asistencias

    context = {
        'alumnos':alumnos,
        'curso':curso
    }   
    return render(request, 'lista_alumnos.html', context)

def listaAsistencias(request, id_alumno):
    asistencia = Asistencia.objects.filter(id_alumno = id_alumno)

    return render(request, 'lista_asistencia.html', {'asistencia':asistencia})