from rest_framework import viewsets, permissions
from prensa.api.serializers import ArticuloListSerializer, ArticuloDetailSerializer
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
