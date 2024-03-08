from django.db import models
from django.contrib.auth.models import User

# Definición de las tablas de precios para la dirección de transporte
# - los valores en el sitio web se actualizarán dinámicamente
#   en función de la información cargada en la base de datos

       
class Valor(models.Model):
    class Meta:
        verbose_name_plural = "valores"
    nombre = models.CharField(
                            max_length=300
                            )
    precio = models.PositiveIntegerField(
                            default=0
                            )
    date_updated = models.DateField(auto_now=True)

    updated_by = models.ForeignKey(
                        User,
                        on_delete=models.SET_NULL,
                        null=True, blank=True,
                        editable=False,
                        related_name="valores_editados")
    def __str__ (self):
        return f'{self.nombre} ${self.precio}'