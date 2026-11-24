from django.urls import include, path
from rest_framework import routers
from Vet_app import views

enrutador = routers.DefaultRouter()
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'mascotas', views.MascotaViewSet)

from .views import (
    landing_page,
    UsuarioListView,
    UsuarioDetailView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    MascotaListView,
    MascotaDetailView,
    MascotaCreateView,
    MascotaUpdateView,
    MascotaDeleteView,
)



urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('api/', include(enrutador.urls)),

        # Rutas Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    # Rutas Mascotas
    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascotas/<int:pk>/editar/', MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', MascotaDeleteView.as_view(), name='mascota_delete'),
]





