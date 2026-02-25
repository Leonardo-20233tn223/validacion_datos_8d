from rest_framework import serializers
from .models import Persona
from datetime import date

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

    def validate_edad(self, value):
        if value < 0:
            raise serializers.ValidationError("La edad no puede ser negativa.")
        return value

    def validate_fecha_nacimiento(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser futura.")
        return value
