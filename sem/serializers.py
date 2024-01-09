from rest_framework import serializers
from sem.models import CertificadoListaBlanca

class CertificadoListaBlancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificadoListaBlanca
        fields = '__all__'