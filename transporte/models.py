from django.db import models
from django.contrib.auth.models import User

# Definición de las tablas de precios para la dirección de transporte
# - los valores en el sitio web se actualizarán dinámicamente
#   en función de la información cargada en la base de datos


class Categoria(models.Model):
    nombre = models.CharField(
                            max_length=300
                            )
    def __str__ (self):
        return self.nombre
       
class Valor(models.Model):
    class Meta:
        verbose_name_plural = "valores"
    
    categoria = models.ForeignKey(
                            Categoria,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name="valores"
                            )
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
                        verbose_name="valores_editados")
    def __str__ (self):
        if self.categoria:
            return f'{self.categoria}: {self.nombre} ${self.precio}'            
        else:
            return f'{self.nombre} ${self.precio}'