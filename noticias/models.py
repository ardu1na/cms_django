from datetime import date
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User   
    
    
class Tag(models.Model):
    nombre=models.CharField(max_length=150, null=False, blank= False)
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre=models.CharField(max_length=150, null=False, blank= False)

    def __str__(self):
        return self.nombre



class Articulo(models.Model):
    titulo=models.CharField(max_length=150, null=False, blank= False)
    fecha=models.DateField(null=True, blank=True, default=date.today)
    autor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulo")

    texto=models.TextField(null=False, blank= False)
    
    imagen=models.ImageField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name="articulos", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulos")

    meta = models.TextField(null=True, blank=True)

    descripcion=models.TextField(null=True, blank= True)

    destacado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)

    slug=models.SlugField(null=True, blank=True, unique=True, editable=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('prensa', args=[str(self.slug)])

    class Meta:
        get_latest_by = "fecha"
        ordering = ["fecha",]
