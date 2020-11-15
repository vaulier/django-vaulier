from django.shortcuts import render
from .models import Producto
from django.utils import timezone

def Catalogo(request):
    productos = Producto.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Vaulier/inicio.html', {'productos' : productos})

def Contacto(request):
    return render(request, 'Vaulier/contactanos.html', {})

def QuienesSomos(request):
    return render(request, 'Vaulier/quienes-somos.html', {})

def Solicitud(request):
    return render(request, 'Vaulier/solicitud.html', {})