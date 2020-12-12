from django.shortcuts import render
from .models import Tejidos 

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    datos= Tejidos.objects.all()
    diccionario = {
        'misTejidos':datos
    }
    return render(request, 'core/formulario.html', diccionario)