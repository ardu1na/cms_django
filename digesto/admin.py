from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from digesto.models import ItemDigesto, Tema, Archivo
from digesto.resources import ItemDigestoResource, TemaResource, ArchivoResource



class ItemDigestoAdmin(ImportExportModelAdmin):
    list_display = ['publicado','numero', 'categoria', 'fecha',   'estado', 'alcance']
    search_fields = ['categoria','numero', 'resumen', 'texto', 'temas__nombre']
    list_filter = ['categoria', 'estado', 'alcance']
    list_display_links = ['numero', 'categoria', 'fecha']
    list_editable = ['publicado',]
    resource_class = ItemDigestoResource
admin.site.register(ItemDigesto, ItemDigestoAdmin)



class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource
admin.site.register(Tema,TemaAdmin)



class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource
admin.site.register(Archivo,ArchivoAdmin)