from django.db import models
from alumnado import models as alumnado_models

# Create your models here.
class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    horaA = models.DateTimeField(auto_now_add=True,verbose_name='Hora')
    id_alumno = models.ForeignKey(alumnado_models.Alumno, on_delete=models.CASCADE, default=0)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.id_alumno, self.id_asistencia)
    