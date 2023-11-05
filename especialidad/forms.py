from django import forms
from .models import Especialidad

class EspecialidadForm(forms.ModelForm):
    nombreEspecialidad = forms.CharField(label = "Nombre de Especialidad")
    disenioCurricular = forms.CharField(label = "Diseño Curricular")
    cantidadMaterias = forms.CharField(label = "Cantidad de Materias")

    class Meta:
        model = Especialidad
        fields = ['id_especialidad', 'nombreEspecialidad', 'disenioCurricular', 'cantidadMaterias']

class EspecialidadFormUpdate(forms.ModelForm):
    nombreEspecialidad = forms.CharField(label = "Nombre de Especialidad")
    disenioCurricular = forms.CharField(label = "Diseño Curricular")
    cantidadMaterias = forms.CharField(label = "Cantidad de Materias")
    
    class Meta:
        model = Especialidad
        fields = ['id_especialidad', 'nombreEspecialidad', 'disenioCurricular', 'cantidadMaterias']