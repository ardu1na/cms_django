from rest_framework import viewsets, permissions, pagination

from cultura.api.serializers import LastEventosListSerializer
from cultura.models import Evento

class EventosPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


## CRUD PRINCIPAL PARA SOLICITUDES PUBLICAS 
class EventosViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.filter(publicado=True).order_by('-fecha')[:5]  
    pagination_class = EventosPagination 
    serializer_class = LastEventosListSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

