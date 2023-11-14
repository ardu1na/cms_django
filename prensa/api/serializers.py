from rest_framework import serializers

from prensa.models import Articulo, Categoria, Tag

## TODO: serializer con titulo , descripcion y sino hay texto cortado, fecha, foto,  de las ultimas tres o cuatro notas o de destacados,




class ArticuloListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id','fecha','titulo', 'descripcion', 'destacado', 'slug']
        
        
class CategoriaListSerializer(serializers.ModelSerializer):
    articulos = ArticuloListSerializer(many=True)
    class Meta:
        model = Categoria
        fields = '__all__'
        

class TagSerializer(serializers.ModelSerializer):
    articulos = ArticuloListSerializer(many=True)

    class Meta:
        model = Tag
        fields = '__all__'
        
        

class ArticuloDetailSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.nombre')
    categoria_id = serializers.ReadOnlyField(source='categoria.id')
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Articulo
        fields = ['id','fecha','titulo','texto', 'meta', 'descripcion', 'slug', 'tags', 'categoria','categoria_id']
        
