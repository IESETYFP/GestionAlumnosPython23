from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Ingresaste correctamente')
            return redirect('index')
        else:
            messages.success(request, 'Hubo un error, ingrese nuevamente')
            return redirect('index')
    else:
        return render(request, 'index.html')


def logout_user(request):
    pass

