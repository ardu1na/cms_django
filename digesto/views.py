
from rest_framework import viewsets, permissions

from digesto.serializers import ItemDigestoListSerializer, ItemDigestoDetailSerializer, TemaSerializer
from digesto.models import ItemDigesto, Tema


## lista de temas de los items dle digesto
class TemasDigestoViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


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