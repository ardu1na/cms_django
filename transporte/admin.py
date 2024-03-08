from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from transporte.models import  Valor
from transporte.resources import ValorResource


class ValorAdmin(ImportExportModelAdmin):
    search_fields = ['nombre',]
    list_display = ['nombre', 'mostrar_precio',]
    list_display_links = ['nombre','mostrar_precio']
    
    resource_class = ValorResource
    def mostrar_precio(self, obj):
        formatted_price = "{:,}".format(obj.precio)
        return f'${formatted_price}'

    mostrar_precio.short_description = 'Precio'

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Valor, ValorAdmin)
