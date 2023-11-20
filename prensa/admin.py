from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from prensa.models import Articulo, Tag
from prensa.forms import ArticuloAdminForm
from prensa.resources import ArticuloResource


## todo: add class into tinymce in order to be able to expand horizontally the rich texteditor


admin.site.register(Tag)



class ArticuloAdmin(ImportExportModelAdmin):
    list_display = ("fecha", "publicado", "titulo", "autor", 'last_editor', 'updated')
    form = ArticuloAdminForm
    resource_class = ArticuloResource

    fieldsets = (
        (None, {'fields': ('publicado','titulo','image_top','texto','image_bottom')},
         ),
        ('Info', {'fields': ('destacado','tags',)},
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

