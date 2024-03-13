
from django.shortcuts import HttpResponsePermanentRedirect
from rest_framework import viewsets, permissions

from transporte.serializers import ValorSerializer
from transporte.models import Valor


## lista de valores de habilitaciones de transporte

class ValorViewSet(viewsets.ModelViewSet):
    queryset = Valor.objects.all()
    serializer_class = ValorSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
