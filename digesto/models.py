from django.db import models
from django.contrib.auth.models import User



class Archivo(models.Model):
    archivo = models.FileField(
                        null=True,
                        blank=True,
                        upload_to='digesto'
    )
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Fuente(models.Model):
    nombre = models.CharField(
                            max_length=200
            )


    def __str__ (self):
        return self.nombre
    

class Boletin(models.Model):
    fecha = models.DateField()
    texto = models.TextField()
    archivo = models.ForeignKey(
                        Archivo,
                        related_name="boletines",
                        on_delete=models.DO_NOTHING, 
                        null=True,
                        blank=True,
                        )
    observaciones = models.TextField(
                        null=True,
                        blank=True
                        )
    fuente = models.ForeignKey(
                        Fuente,
                        related_name="boletines",
                        null=True,
                        blank=True,
                        on_delete=models.DO_NOTHING
                        )
    publicado = models.BooleanField(default=True)

    date_updated = models.DateField(auto_now=True)

    updated_by = models.ForeignKey(
                        User,
                        on_delete=models.SET_NULL,
                        null=True, blank=True,
                        editable=False,
                        verbose_name="items_editados")
    
    @property
    def get_fecha(self):
        fecha = self.fecha.strftime('%d/%m/%y') if self.fecha else ''
        return fecha
    
    def __str__ (self):
        return f'Boletín del {self.get_fecha}'

    class Meta:
        verbose_name = "Boletín"
        verbose_name_plural = "Boletines"
        


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
    DECLARACION = 'declaración'
    BOLETIN = 'boletín'
    ANEXO = 'anexo'

    CATEGORIA_CHOICES = (
        (ORDENANZA, ('ordenanza')),
        (RESOLUCION, ('resolución')),
        (COMUNICADO, ('comunicado')),
        (DECLARACION, ('declaración')),
        (BOLETIN, ('boletín')),
        (ANEXO, ('anexo')),

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


    numero = models.CharField(
                        max_length=50,
                        null=True,
                        blank=True
                        )

    temas = models.ManyToManyField(
                        Tema,
                        related_name="items",
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

    texto = models.TextField(
                        null= True,
                        blank = True,
                        )
    archivo = models.ForeignKey(Archivo, on_delete=models.DO_NOTHING, related_name="items", null=True,
                        blank=True)

    observaciones = models.TextField(
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


    publicado = models.BooleanField(default=True)

    date_updated = models.DateField(auto_now=True)

    updated_by = models.ForeignKey(
                        User,
                        on_delete=models.SET_NULL,
                        null=True, blank=True,
                        editable=False)

    fuente = models.ForeignKey(
                        Fuente,
                        related_name="items",
                        null=True,
                        blank=True,
                        on_delete=models.DO_NOTHING
                        )



    @property
    def anio(self):
        return self.fecha.year


    def __str__ (self):
        return f'{self.anio} - {self.categoria} n° {self.numero}'

    class Meta:
        verbose_name = "Elemento del Digesto"
        verbose_name_plural = "Elementos del Digesto"
        unique_together  = [ ['numero', 'categoria'
        ],]
