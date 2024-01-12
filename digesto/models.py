from django.db import models



class Tema(models.Model):
    nombre = models.CharField(
                            max_length=200
            )
    
    
    def __str__ (self):
        return self.nombre


class ItemDigesto (models.Model):
    ORDENANZA = 'ordenanza'
    RESOLUCION = 'resolución'
    COMUNICADO = 'comunicado'
    DECLARACION = 'declaración de interés'

    CATEGORIA_CHOICES = (
        (ORDENANZA, ('ordenanza')),
        (RESOLUCION, ('resolución')),
        (COMUNICADO, ('modificada')),
        (DECLARACION, ('comunicado de interés')),
        
    )

    EN_VIGENCIA = 'en vigencia'
    DEROGADA = 'derogada'
    MODIFICADA = 'modificada'
    
    ESTADO_CHOICES = (
        (EN_VIGENCIA, ('en vigencia')),
        (DEROGADA, ('derogada')),
        (MODIFICADA, ('modificada')),
    )

    GENERAL = 'general'
    PARTICULAR = 'particular'
    
    ALCANCE_CHOICES = (
        (GENERAL, ('general')),
        (PARTICULAR, ('particular')),
    )



    categoria = models.CharField(
                        max_length=50,
                        choices=CATEGORIA_CHOICES,
                        )
    
    fecha = models.DateField(
                        )
    
    titulo = models.CharField(
                        max_length=200,
                        )
    
    numero = models.CharField(
                        max_length=50,
                        null=True,
                        blank=True
                        )
    
    tema = models.ManyToManyField(
                        Tema,
                        related_name="ordenanzas",
                        null=True,
                        blank=True
                        )
    estado = models.CharField(
                        max_length=50,
                        choices=ESTADO_CHOICES,
                        null=True,
                        blank=True
                        )
    alcance = models.CharField(
                        max_length=50,
                        choices=ALCANCE_CHOICES,
                        null=True,
                        blank=True
                        )
    observaciones = models.TextField(
                        null=True,
                        blank=True
                        )
    resumen = models.TextField(
                        null=True,
                        blank=True
                        )
    modifica_a = models.ManyToManyField(
                        'ItemDigesto',
                        related_name="modificada_por",
                        null=True,
                        blank=True
                        )
    cita_a = models.ManyToManyField(
                        'ItemDigesto',
                        related_name="citada_por",
                        null=True,
                        blank=True
                        )
    texto = models.TextField(
                        null= True,
                        blank = True,
                        )
    archivo = models.FileField(
                        null=True,
                        blank=True,
                        upload_to='digesto'
    )

    
    @property
    def anio(self):
        return self.fecha.year

    def __str__ (self):
        return f'{self.anio} - {self.categoria} n° {self.numero} - {self.titulo}'
    
    class Meta:
        verbose_name = "Item del Digesto Municipal"
        verbose_name_plural = "Items del Digesto Municipal"
