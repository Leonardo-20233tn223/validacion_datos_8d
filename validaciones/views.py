from django.shortcuts import render
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer

# Create your views here.
def index(request):
    return render(request, 'validaciones/index.html')

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
