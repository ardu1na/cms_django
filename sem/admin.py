from django.contrib import admin
from sem.models import CertificadoListaBlanca
from sem.resources import CertificadoListaBlancaResource
from import_export.admin import ImportExportModelAdmin



class CertificadoAdmin(ImportExportModelAdmin):
    list_display = ("patente", "dni", "apellido", "nombre")
    resource_class = CertificadoListaBlancaResource
   



admin.site.register(CertificadoListaBlanca, CertificadoAdmin)
