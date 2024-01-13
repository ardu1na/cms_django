from rest_framework import serializers
from digesto.models import ItemDigesto, Tema

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'

class ItemDigestoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDigesto
        fields = ['id', 'categoria', 'anio', 'numero', 'titulo', 'temas', 'estado', 'alcance']



class ItemDigestoDetailSerializer(serializers.ModelSerializer):
    temas = serializers.SerializerMethodField()

    class Meta:
        model = ItemDigesto
        fields = ['id', 'categoria', 'fecha', 'anio', 'titulo', 'numero', 'temas', 'estado', 'alcance', 'observaciones', 'resumen', 'modifica_a', 'cita_a','texto','archivo']

    
