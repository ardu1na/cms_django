from rest_framework import viewsets
from sem.models import CertificadoListaBlanca, Exento
from sem.serializers import CertificadoListaBlancaSerializer, ExentoSerializer

class CertificadoListaBlancaViewSet(viewsets.ModelViewSet):
    queryset = CertificadoListaBlanca.objects.all()
    serializer_class = CertificadoListaBlancaSerializer




class ExentoViewSet(viewsets.ModelViewSet):
    queryset = Exento.objects.all()
    serializer_class = ExentoSerializer
