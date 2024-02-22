from django.contrib import admin
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin

from cultura.models import Evento
from cultura.resources import EventoResource



class EventoAdmin(ImportExportModelAdmin):
    list_display = ("publicado", "titulo", "fecha", "display_image")
    resource_class = EventoResource
    list_per_page = 5
    list_display_links = ["publicado", "titulo", "fecha"]
    
    def display_image(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen.url)
        return "Sin Imagen"

    display_image.short_description = "Imagen"

    search_fields=["titulo",'descripcion']
    list_filter=['publicado']
    
    def save_model(self, request, obj, form, change):
        if obj.autor == None:
            obj.autor = request.user
        obj.save()

admin.site.register(Evento, EventoAdmin)

