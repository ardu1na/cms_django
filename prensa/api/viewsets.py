
from rest_framework import viewsets
from prensa.api.serializers import ArticuloListSerializer,  ArticuloDetailSerializer
from prensa.models import Articulo

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.filter(publicado=True)
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticuloListSerializer
        return ArticuloDetailSerializer