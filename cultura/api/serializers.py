from datetime import datetime
from rest_framework import serializers
from cultura.models import Evento

def get_formatted_date(fecha):
    return datetime.strftime(fecha, "%d/%m/%Y %H:%M hs.")

class LastEventosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion', 'imagen', 'date']
    
    def get_date(self, obj):
        return get_formatted_date(obj.fecha)
    
