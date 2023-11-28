from datetime import datetime
from rest_framework import serializers
from prensa.models import Articulo, Tag

def get_formatted_date(fecha):
    return datetime.strftime(fecha, "%d/%m/%Y %H:%M hs.")

class LastArticulosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'titulo']

class CardArticulosSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = ['id', 'date', 'titulo', 'image_top', 'image_bottom', 'destacado', 'slug']

    def get_date(self, obj):
        return get_formatted_date(obj.fecha)

class ArticuloListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'fecha', 'titulo', 'destacado', 'slug']

class TagSerializer(serializers.ModelSerializer):
    articulos = ArticuloListSerializer(many=True)

    class Meta:
        model = Tag
        fields = '__all__'

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nombre']

class ArticuloDetailSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Articulo
        fields = ['id', 'date', 'titulo', 'texto', 'meta', 'slug', 'tags', 'image_top', 'image_bottom']

    def get_date(self, obj):
        return get_formatted_date(obj.fecha)
