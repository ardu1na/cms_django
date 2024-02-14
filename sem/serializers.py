from rest_framework import serializers
from sem.models import CertificadoListaBlanca, Exento

class CertificadoListaBlancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificadoListaBlanca
        fields = '__all__'



class ExentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exento
        fields = '__all__'