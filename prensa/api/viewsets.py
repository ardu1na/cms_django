from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from prensa.api.serializers import ArticuloListSerializer, ArticuloDetailSerializer, LastArticulosSerializer
from prensa.models import Articulo

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
    


    
@api_view(['GET'])
def lastArticulosView(request):
    last_articulos = Articulo.objects.filter(publicado=True).order_by('-fecha')[:3]  
    serializer = LastArticulosSerializer(last_articulos, many=True)  
    return Response(serializer.data)  

