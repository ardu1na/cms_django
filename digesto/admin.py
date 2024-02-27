from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from digesto.models import ItemDigesto, Tema, Archivo, Fuente, Boletin
from digesto.resources import ItemDigestoResource, TemaResource, ArchivoResource, FuenteResource


class ItemDigestoAdmin(ImportExportModelAdmin):
    list_display = ['custom_categoria_numero', 'formatted_fecha', 'alcance', 'display_temas']
    search_fields = ['categoria', 'numero', 'texto', 'temas__nombre']
    list_filter = ['categoria', 'estado', 'alcance', 'temas']
    list_display_links = ['custom_categoria_numero', 'formatted_fecha', 'alcance']
    resource_class = ItemDigestoResource

    def custom_categoria_numero(self, obj):
        return f'{obj.categoria.capitalize()} {obj.numero}'
    custom_categoria_numero.short_description = 'Objeto'

    def display_temas(self, obj):
        return ', '.join([tema.nombre for tema in obj.temas.all()])
    display_temas.short_description = 'Temas'

    def formatted_fecha(self, obj):
        return obj.fecha.strftime('%d/%m/%y') if obj.fecha else ''
    formatted_fecha.short_description = 'Fecha'

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    change_list_title = "Digesto Municipal"
admin.site.register(ItemDigesto, ItemDigestoAdmin)


class BoletinAdmin(admin.ModelAdmin):
    search_fields = ['texto',]


    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Boletin, BoletinAdmin)


class FuenteAdmin(ImportExportModelAdmin):
    resource_class = FuenteResource
admin.site.register(Fuente, FuenteAdmin)

class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource
admin.site.register(Tema, TemaAdmin)



class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource
admin.site.register(Archivo, ArchivoAdmin)