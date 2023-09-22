from django.db import models
from django.db.models.fields.files import ImageField
from profesores import models as profesores_models

# Create your models here.

class Agenda(models.Model):
    fechaHora = models.DateTimeField()
    descripcion = models.TextField()
    id_profesor = models.ForeignKey(profesores_models.Profesor, on_delete=models.CASCADE, default=0)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id_profesor)