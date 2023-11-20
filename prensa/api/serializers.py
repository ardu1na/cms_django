from rest_framework import serializers

from prensa.models import Articulo, Tag

## TODO: serializer con titulo , sino hay texto cortado, fecha, foto,  de las ultimas tres o cuatro notas o de destacados,




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
        fields = ['id','fecha','titulo','texto', 'meta', 'slug', 'tags']
        
