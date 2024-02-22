from datetime import datetime
from rest_framework import serializers
from cultura.models import Evento

class LastEventosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion', 'imagen', 'fecha']
    
    
