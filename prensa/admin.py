from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from prensa.models import Categoria, Articulo, Tag
from prensa.forms import ArticuloAdminForm
from prensa.resources import ArticuloResource

admin.site.register(Categoria)
admin.site.register(Tag)


## todo: add class into tinymce in order to be able to expand horizontally the rich texteditor


class ArticuloAdmin(ImportExportModelAdmin):
    list_display = ("fecha", "publicado", "titulo", "categoria", "descripcion","autor", 'last_editor', 'updated')
    form = ArticuloAdminForm
    resource_class = ArticuloResource

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

