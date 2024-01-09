from django.db import models


class CertificadoListaBlanca(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=False, blank=False)
    dni = models.IntegerField(null=False, blank=False)
    patente = models.CharField(max_length=200, null=False, blank=False)
    certificado = models.FileField(null=False, blank=False)

    def __str__(self):
        return f'PATENTE: {self.patente} - {self.apellido}, {self.nombre} DNI {self.dni}'