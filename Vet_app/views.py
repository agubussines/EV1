from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario, Mascota
from .serializer import UsuarioSerializer, MascotaSerializer

# Create your views here.
def landing_page(request):
    # Esto le dice a Django que renderice el archivo hindex.html
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer





