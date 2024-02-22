from rest_framework import viewsets, permissions

from cultura.api.serializers import LastEventosListSerializer
from cultura.models import Evento


## CRUD PRINCIPAL PARA SOLICITUDES PUBLICAS 
class EventosViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.filter(publicado=True).order_by('-fecha')[:5]  
    serializer_class = LastEventosListSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

