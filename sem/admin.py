from django.contrib import admin
from sem.models import CertificadoListaBlanca, Exento
from sem.resources import CertificadoListaBlancaResource, ExentoResource
from import_export.admin import ImportExportModelAdmin



class CertificadoAdmin(ImportExportModelAdmin):
    list_display = ("patente", "dni", "apellido", "nombre")
    resource_class = CertificadoListaBlancaResource
   



admin.site.register(CertificadoListaBlanca, CertificadoAdmin)



class ExentoAdmin(ImportExportModelAdmin):
    list_display = ("propietario", "dominio", "marca", "modelo", "modelo_anio", "tipo")
    resource_class = ExentoResource
   



admin.site.register(Exento, ExentoAdmin)
