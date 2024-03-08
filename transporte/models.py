from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=300)
    
class Valor(models.Model):
    class Meta:
        verbose_name_plural = "valores"
    
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=300)
    precio = models.PositiveIntegerField(default=0)