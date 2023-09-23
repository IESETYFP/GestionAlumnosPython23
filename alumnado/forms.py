from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Alumno
        fields = ['id_alumno', 'dni_a', 'cuil_a',
                  'apellido_a', 'nombre_a', 'matricula', 
                  'tutores', 'telefono', 'direccion', 
                  'fecha_nac', 'copiaDNI_A', 'id_curso']

class AlumnoFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'dni_a', 'cuil_a',
                  'apellido_a', 'nombre_a', 'matricula', 
                  'tutores', 'telefono', 'direccion', 
                  'fecha_nac', 'copiaDNI_A', 'id_curso']