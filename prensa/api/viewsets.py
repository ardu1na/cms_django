from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from prensa.api.serializers import ArticuloListSerializer, ArticuloDetailSerializer,\
      CardArticulosSerializer, LastArticulosListSerializer, TagListSerializer
from prensa.models import Articulo, Tag



## CRUD PRINCIPAL PARA SOLICITUDES PUBLICAS 
class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.filter(publicado=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticuloListSerializer
        return ArticuloDetailSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    





## DEVUELVE LA DATA PARA LAS TARJETAS ##
# ARTICULOS DESTACADOS 
@api_view(['GET'])
def DestacadosArticulosView(request):
    articulos_destacados = Articulo.objects.filter(publicado=True, destacado=True).order_by('-fecha')[:3]  
    serializer = CardArticulosSerializer(articulos_destacados, many=True)  
    return Response(serializer.data)  

# ULTIMAS NOTICIAS    
@api_view(['GET'])
def lastArticulosView(request):
    last_articulos = Articulo.objects.filter(publicado=True).order_by('-fecha')[:3]  
    serializer = CardArticulosSerializer(last_articulos, many=True)  
    return Response(serializer.data)  






## DEVUELVE LA LISTA DE TITULOS DE LOS ÚLTIMOS ARTICLOS
@api_view(['GET'])
def lastArticulosList(request):
    last_articulos = Articulo.objects.filter(publicado=True).order_by('-fecha')[:7]  
    serializer = LastArticulosListSerializer(last_articulos, many=True)  
    return Response(serializer.data)  

## DEVUELVE LA LISTA DE tags 
@api_view(['GET'])
def tagsList(request):
    tags = Tag.objects.all[:10]  
    serializer = TagListSerializer(tags, many=True)  
    return Response(serializer.data)  