from django.contrib import admin

from noticias.models import Categoria, Articulo, Tag
from noticias.forms import ArticuloAdminForm


admin.site.register(Categoria)
admin.site.register(Tag)


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("fecha", "titulo")
    form = ArticuloAdminForm

    def save_model(self, request, obj, form, change):
        if obj.autor == None:
            obj.autor = request.user
        obj.last_editor = request.user
        obj.save()

admin.site.register(Articulo, ArticuloAdmin)