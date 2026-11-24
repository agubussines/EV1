from django import forms
from .models import Usuario, Mascota


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'correo',
            'contrasena',
            'genero',
            'nacionalidad',
            'fechaNacimiento',
            'calle',
            'numero',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del dueño',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.cl',
            }),
            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una contraseña',
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Femenino, Masculino, No binario',
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Chilena',
            }),
            'fechaNacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'calle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la calle',
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'N° de domicilio / depto',
            }),
        }


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'usuario',
            'nombre',
            'especie',
            'raza',
            'edad',
            'peso',
            'color',
            'sexo',
            'fechaNacimiento',
            'observaciones',
        ]
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'form-select',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la mascota',
            }),
            'especie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Perro, Gato',
            }),
            'raza': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Mestizo, Poodle',
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': 'Edad en años',
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Peso en kg',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Color del pelaje',
            }),
            'sexo': forms.Select(
                choices=[
                    ('Macho', 'Macho'),
                    ('Hembra', 'Hembra'),
                ],
                attrs={'class': 'form-select'},
            ),
            'fechaNacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Alergias, vacunas o notas clínicas...',
            }),
        }