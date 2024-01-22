from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from digesto.models import ItemDigesto, Tema, Archivo
from digesto.resources import ItemDigestoResource, TemaResource, ArchivoResource



class ItemDigestoAdmin(ImportExportModelAdmin):
    list_display = ['categoria', 'numero',  'fecha', 'alcance']
    search_fields = ['categoria','numero', 'observaciones', 'texto', 'temas__nombre']
    list_filter = ['categoria', 'estado', 'alcance']
    list_display_links = ['numero', 'categoria', 'fecha']
    resource_class = ItemDigestoResource
admin.site.register(ItemDigesto, ItemDigestoAdmin)



class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource
admin.site.register(Tema,TemaAdmin)



class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource
admin.site.register(Archivo,ArchivoAdmin)