from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.asistencia, name='asistencia'),
    path('listaAlumnos/<id_curso>', views.listaAlumnos, name='listaAlumnos'),
    path('listasAsistencias/<id_alumno>', views.listaAsistencias, name='listaAsistencias')
]