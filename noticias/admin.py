from django.contrib import admin

from noticias.models import Categoria, Articulo, Tag
from noticias.forms import ArticuloAdminForm


admin.site.register(Categoria)
admin.site.register(Tag)


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("fecha", "titulo")
    form = ArticuloAdminForm

admin.site.register(Articulo, ArticuloAdmin)