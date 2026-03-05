from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer
from .forms import PersonaForm

# Create your views here.
def index(request):
    """Display form and handle submission with back-end validation."""
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            # after successful save we can reset the form and show a success flag
            return render(request, 'validaciones/index.html', {
                'form': PersonaForm(),
                'success': True
            })
    else:
        form = PersonaForm()

    return render(request, 'validaciones/index.html', {'form': form})

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
