from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    """Form para la entidad Persona con validación adicional."""

    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellido1',
            'apellido2',
            'edad',
            'fecha_nacimiento',
            'email',
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'apellido1': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'apellido2': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'min': '0'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad is not None and edad < 0:
            raise forms.ValidationError("La edad debe ser un número positivo.")
        return edad

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Persona.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
