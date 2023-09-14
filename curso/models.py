from django.db import models

# Create your models here.
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    Annio = models.CharField(max_length=5)
    Division = models.CharField(max_length=4)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombreCurso)