from django.shortcuts import render, redirect
from .models import Especialidad
from .forms import EspecialidadForm

# Create your views here.
def especialidad(request):
    especialidad_form = EspecialidadForm()
    especialidad = Especialidad.objects.all()


    if request.method == 'POST':
        especialidad_form = EspecialidadForm(data=request.POST)

        if especialidad_form.is_valid():
            especialidad_form.save()
            return redirect('/especialidad')

    context = {
        'especialidad_form' :especialidad_form,
        'especialidad': especialidad
    }
    return render(request, 'gestion_especialidad.html', context)
