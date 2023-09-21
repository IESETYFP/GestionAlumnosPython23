from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.curso, name='curso'),
    #path('verAsistencia/<id_asistencia>', views.verAsistencia, name='ver_asistencia'),
    path('editarCurso/<id_curso>/', views.editarCurso, name='editar_curso'),
    path('eliminarCurso/<id_curso>/', views.eliminarCurso, name='eliminar_curso'),
]