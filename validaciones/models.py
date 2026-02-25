from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellido1 = models.CharField(max_length=100, blank=False, null=False)
    apellido2 = models.CharField(max_length=100, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self): 
        return f"{self.nombres} {self.apellido1}"
