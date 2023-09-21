from django import forms
from .models import Notas

from alumnado.models import Alumno
from materias.models import Materia

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['id_nota', 'valor', 'fechaNota', 'AnnioCursada', 'id_materia', 'id_alumno']

class NotasFormUpdate(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['id_nota', 'valor', 'fechaNota', 'AnnioCursada', 'id_materia', 'id_alumno']
