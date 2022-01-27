from rest_framework import serializers
from .models import Vehiculo 

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria']