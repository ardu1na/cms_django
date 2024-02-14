from django.contrib import admin
from sem.models import Exento
from sem.resources import ExentoResource
from import_export.admin import ImportExportModelAdmin




class ExentoAdmin(ImportExportModelAdmin):
    list_display = ("propietario", "dominio", "marca", "modelo", "modelo_anio", "tipo")
    resource_class = ExentoResource




admin.site.register(Exento, ExentoAdmin)
