from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User   
from django.urls import reverse

class Evento(models.Model):
    titulo = models.CharField(
        max_length=150,
        null=False, blank= False)
    
    
    
    imagen = models.ImageField(upload_to="eventos")
    descripcion = models.TextField(null=True, blank= True, verbose_name="descripción") 
    fecha = models.DateTimeField(null=True, blank=True)
    
    publicado = models.BooleanField(default=False)

    autor = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            null=True, blank= True,
            related_name="eventos",
            editable=False
            )
    
    slug = models.SlugField(
            max_length=150,
            null=True, blank=True,
            unique=True,
            editable=False
            )
    
    def get_absolute_url(self):
        return reverse('articulo', args=[str(self.slug)])

    class Meta:
        get_latest_by = "fecha"
        ordering = ["fecha",]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo