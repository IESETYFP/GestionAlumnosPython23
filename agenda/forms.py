from django import forms
from .models import Agenda

from profesores.models import Profesor

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'