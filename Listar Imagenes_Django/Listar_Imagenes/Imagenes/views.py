from django.shortcuts import render, redirect
from .forms import ImagenForm

# Create your views here.
from django.shortcuts import render
from .models import Imagen

def listar_imagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'listar_imagenes.html', {'imagenes': imagenes})


def cargar_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_imagenes')
    else:
        form = ImagenForm()
    return render(request, 'cargar_imagen.html', {'form': form})
