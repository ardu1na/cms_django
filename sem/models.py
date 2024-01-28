from django.db import models


class CertificadoListaBlanca(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=False, blank=False)
    dni = models.IntegerField(null=False, blank=False)
    patente = models.CharField(max_length=200, null=False, blank=False)
    certificado = models.FileField(null=False, blank=False)

    def __str__(self):
        return f'PATENTE: {self.patente} - {self.apellido}, {self.nombre} DNI {self.dni}'
    

class Exento(models.Model):
    AUTO = 'auto'
    CAMIONETA = 'camioneta'

    VEHICLE_CHOICES = [
        (AUTO, 'Auto'),
        (CAMIONETA, 'Camioneta'),
    ]

    propietario = models.CharField(max_length=200, null=False, blank=False)
    dominio = models.CharField(max_length=200, null=False, blank=False)
    marca = models.CharField(max_length=200, null=False, blank=False)
    modelo = models.CharField(max_length=200, null=False, blank=False)
    modelo_anio = models.CharField(max_length=200, null=False, blank=False, verbose_name="modelo/año")
    tipo = models.CharField(max_length=200, null=False, blank=False, choices=VEHICLE_CHOICES)
    certificado = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'PATENTE: {self.dominio} - {self.propietario}'
    
    class Meta:
        verbose_name= "Vehículo exento"
        verbose_name_plural= "Vehículos exentos"
    
