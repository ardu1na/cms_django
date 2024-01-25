from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from digesto.models import ItemDigesto, Tema, Archivo
from digesto.resources import ItemDigestoResource, TemaResource, ArchivoResource


class ItemDigestoAdmin(ImportExportModelAdmin):
    list_display = ['custom_categoria_numero', 'fecha', 'alcance', 'display_temas']
    search_fields = ['categoria', 'numero', 'observaciones', 'texto', 'temas__nombre']
    list_filter = ['categoria', 'estado', 'alcance', 'temas']
    list_display_links = ['custom_categoria_numero', 'fecha', 'alcance']
    resource_class = ItemDigestoResource

    def custom_categoria_numero(self, obj):
        return f'{obj.categoria.capitalize()} {obj.numero}'
    custom_categoria_numero.short_description = 'Objeto'

    def display_temas(self, obj):
        return ', '.join([tema.nombre for tema in obj.temas.all()])
    display_temas.short_description = 'Temas'

admin.site.register(ItemDigesto, ItemDigestoAdmin)




class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource
admin.site.register(Tema,TemaAdmin)



class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource
admin.site.register(Archivo,ArchivoAdmin)