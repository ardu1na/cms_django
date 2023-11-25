from datetime import datetime

from rest_framework import serializers

from prensa.models import Articulo, Tag


class LastArticulosSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = ['id','date','titulo', 'image_top', 'image_bottom', 'destacado', 'slug']

    def get_date(self, obj):
        fecha = obj.fecha
        formatted_date = datetime.strftime(fecha, "%d/%m/%Y %H:%M hs.")
        return formatted_date
        
     
class ArticuloListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id','fecha','titulo', 'destacado', 'slug']
        
        
class TagSerializer(serializers.ModelSerializer):
    articulos = ArticuloListSerializer(many=True)

    class Meta:
        model = Tag
        fields = '__all__'
        
        

class ArticuloDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Articulo
        fields = ['id','fecha','titulo','texto', 'meta', 'slug', 'tags', 'image_top', 'image_bottom',]
        
