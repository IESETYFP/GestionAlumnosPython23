from django.db import models
from django.db.models.fields.files import ImageField
from curso import models as curso_models

# Create your models here.
options = [
    [0, 'Regular'],
    [1, 'Semipresencial'],
    [2, 'Libre'],
]
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    dni_a = models.CharField(max_length=9)
    cuil_a = models.CharField(max_length=15)
    apellido_a = models.CharField(max_length=50)
    nombre_a = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    tutores = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    fecha_nac = models.DateField(blank=True)
    copiaDNI_A = ImageField(blank=True, null=True, upload_to='alumnado/images/')
    condicion = models.IntegerField(choices=options, null=True, verbose_name='Condición')
    turno = models.CharField(max_length=30, null=True, blank=True, verbose_name='Turno')
    cantidad_asistencias= models.IntegerField(default=0)
    cantidad_inasistencias= models.IntegerField(default=0)
    id_curso = models.ForeignKey(curso_models.Curso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.apellido_a, self.nombre_a, self.id_alumno)

