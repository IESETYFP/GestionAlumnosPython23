from django.db import models
from materia import models as materia_models

# Create your models here.

class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    dni_p = models.CharField(max_length=9)
    cuil_p = models.CharField(max_length=15)
    apellido_p = models.CharField(max_length=50)
    nombre_p = models.CharField(max_length=50)
    legajo_p = models.CharField(max_length=10, blank=True, null=True)
    telefono_p = models.CharField(max_length=20, blank=True, null=True)
    direccion_p = models.CharField(max_length=50, blank=True, null=True)
    fecha_nac_p = models.DateField(blank=True, null=True)
    copiaDNI_p = models.ImageField(upload_to='personal/images/', blank=True, null=True)
    rol_p = models.CharField(max_length=50, blank=True, null=True)
    id_materia = models.ForeignKey(materia_models.Materia, on_delete=models.CASCADE, default=0)

    def __str__(self):
        texto = "{0}, {1} ({2})"
        return texto.format(self.apellido_p, self.nombre_p, self.id_personal)