from django.contrib import admin

from .models import Mascota, Usuario

admin.site.register(Usuario)
admin.site.register(Mascota)
