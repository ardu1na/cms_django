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
    
    fecha = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulos", editable=False)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulos_editados", editable=False)
    
    titulo = models.CharField(max_length=150, null=False, blank= False, unique=True)
    image_top = models.ImageField(upload_to="posts", null=True, blank= True)
    texto = models.TextField(null=True, blank= True) 
    descripcion = models.TextField(null=True, blank= True)

    image_bottom = models.ImageField(upload_to="posts",null=True, blank= True)
   
    
    tags = models.ManyToManyField(Tag, related_name="articulos", blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulos")

    meta = models.TextField(null=True, blank=True)


    destacado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)

    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)


    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.titulo)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('prensa', args=[str(self.slug)])

    class Meta:
        get_latest_by = "fecha"
        ordering = ["fecha",]
