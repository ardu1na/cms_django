
from rest_framework import viewsets, permissions
from django.http import JsonResponse

from transporte.serializers import ValorSerializer
from transporte.models import Valor, Visita


## lista de valores de habilitaciones de transporte

class ValorViewSet(viewsets.ModelViewSet):
    queryset = Valor.objects.all()
    serializer_class = ValorSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
## contador de viistas a la pag

def actualizar_visita(request):
    visita, created = Visita.objects.get_or_create(pk=1)
    visita.save()
    return JsonResponse({'cantidad': visita.cantidad})
