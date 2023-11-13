from django.contrib import admin

from prensa.models import Categoria, Articulo, Tag
from prensa.forms import ArticuloAdminForm


admin.site.register(Categoria)
admin.site.register(Tag)


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("fecha", "titulo", "categoria", "descripcion","autor", 'last_editor', 'updated')
    form = ArticuloAdminForm
    fieldsets = (
        (None, {'fields': ('publicado','titulo','image_top','texto','image_bottom')},
         ),
        ('Info', {'fields': ('descripcion', 'destacado','tags','categoria')},
         ),
        ('Meta', {'fields': ('meta',)},
         ),
    )
    def save_model(self, request, obj, form, change):
        if obj.autor == None:
            obj.autor = request.user
        if obj.pk != None:
            obj.last_editor = request.user
        obj.save()

admin.site.register(Articulo, ArticuloAdmin)


## TODO:
# - display as '(borrador)' in title when SELF.PUBLISHED = FALSE
# - display image preview in changeform

