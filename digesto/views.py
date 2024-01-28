
from rest_framework import viewsets, permissions

from digesto.serializers import ItemDigestoListSerializer, ItemDigestoDetailSerializer
from digesto.models import ItemDigesto



## CRUD PRINCIPAL PARA SOLICITUDES PUBLICAS 
class DigestoViewSet(viewsets.ModelViewSet):
    queryset = ItemDigesto.objects.filter(publicado=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ItemDigestoListSerializer
        return ItemDigestoDetailSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]