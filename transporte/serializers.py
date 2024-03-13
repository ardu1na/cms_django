from rest_framework import serializers
from transporte.models import Valor


class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = ['id', 'nombre', 'precio', 'slug']


