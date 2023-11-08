from django import forms
from .models import Asistencia

from alumnado.models import Alumno

class AsistenciaForm(forms.ModelForm):

    class Meta:
        model = Asistencia
        fields = ['id_alumno']
    
class AsistenciaFormUpdate(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['id_alumno']
