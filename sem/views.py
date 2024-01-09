from rest_framework import viewsets
from sem.models import CertificadoListaBlanca
from sem.serializers import CertificadoListaBlancaSerializer

class CertificadoListaBlancaViewSet(viewsets.ModelViewSet):
    queryset = CertificadoListaBlanca.objects.all()
    serializer_class = CertificadoListaBlancaSerializer
