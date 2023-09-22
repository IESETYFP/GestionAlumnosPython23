from django.urls import path
from . import views

app_name = 'especialidad'

urlpatterns = [
    path('', views.especialidad, name='especialidad'),
    #path('verAsistencia/<id_asistencia>', views.verAsistencia, name='ver_asistencia'),
    #path('editarAsistencia/<id_asistencia>/', views.editarAsistencia, name='editar_asistencia'),
    #path('eliminarAsistencia/<id_asistencia>/', views.eliminarAsistencia, name='eliminar_asistencia'),
]