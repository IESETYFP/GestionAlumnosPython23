from django import forms
from .models import Especialidad

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['id_nota', 'valor', 'fechaNota', 'AnnioCursada', 'id_materia', 'id_alumno']
