from django.db import models
from profesores import models as profesores_models
from curso import models as curso_models
from especialidad import models as especialidad_models

# Create your models here.

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombreMateria = models.CharField(max_length=50)
    id_curso = models.ForeignKey(curso_models.Curso, on_delete=models.CASCADE)
    id_profesores = models.ForeignKey(profesores_models.Profesor, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(especialidad_models.Especialidad, on_delete=models.CASCADE, null=True)
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombreMateria)