from django.shortcuts import render
from rest_framework import viewsets

from .models import Mascota, Usuario
from .serializer import MascotaSerializer, UsuarioSerializer

def landing_page(request):
    return render(request, 'index.html')


def inicio(request):
    return render(request, 'inicio.html')


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Usuario, Mascota
from .forms import UsuarioForm, MascotaForm


def landing_page(request):
    return render(request, 'index.html')


# ==========================================
# CRUD WEB USUARIOS (CBV)
# ==========================================
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'
    context_object_name = 'usuario'


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('usuario_list')


# ==========================================
# CRUD WEB MASCOTAS (CBV)
# ==========================================
class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascotas/mascota_list.html'
    context_object_name = 'mascotas'

    def get_queryset(self):
        return Mascota.objects.select_related('usuario')


class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'mascotas/mascota_detail.html'
    context_object_name = 'mascota'


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_confirm_delete.html'
    context_object_name = 'mascota'
    success_url = reverse_lazy('mascota_list')