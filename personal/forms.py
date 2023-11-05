from django import forms
from .models import Personal


class PersonalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac_p'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        self.fields['legajo_p'].required = False
        self.fields['telefono_p'].required = False
        self.fields['direccion_p'].required = False
        self.fields['copiaDNI_p'].required = False
        self.fields['fecha_nac_p'].required = False
    
    dni_p = forms.CharField(label="DNI")
    cuil_p = forms.CharField(label="CUIL")
    apellido_p = forms.CharField(label="Apellido del Personal")
    nombre_p = forms.CharField(label="Nombre del Personal")
    copiaDNI_p = forms.ImageField(label="Copia de DNI")
    fecha_nac_p = forms.DateField(label="Fecha de Nacimiento")
    telefono_p = forms.CharField(label="Teléfono")
    direccion_p = forms.CharField(label="Dirección")
    legajo_p = forms.CharField(label="Legajo")
    rol_p = forms.CharField(label="Rol del Personal")


    class Meta:
        model = Personal
        fields = ['id_personal', 'dni_p', 'cuil_p', 'apellido_p', 'nombre_p',
                  'legajo_p', 'telefono_p', 'direccion_p', 'fecha_nac_p', 'copiaDNI_p', 'rol_p', 'id_materia']


class PersonalFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac_p'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
        self.fields['copiaDNI_p'].required = False
        self.fields['fecha_nac_p'].required = False
    

    dni_p = forms.CharField(label="DNI")
    cuil_p = forms.CharField(label="CUIL")
    apellido_p = forms.CharField(label="Apellido del Personal")
    nombre_p = forms.CharField(label="Nombre del Personal")
    copiaDNI_p = forms.ImageField(label="Copia de DNI")
    fecha_nac_p = forms.DateField(label="Fecha de Nacimiento")
    telefono_p = forms.CharField(label="Teléfono")
    direccion_p = forms.CharField(label="Dirección")
    legajo_p = forms.CharField(label="Legajo")

    class Meta:
        model = Personal
        fields = ['id_personal', 'dni_p', 'cuil_p', 'apellido_p', 'nombre_p',
                  'legajo_p', 'telefono_p', 'direccion_p', 'fecha_nac_p', 'copiaDNI_p', 'rol_p', 'id_materia']
