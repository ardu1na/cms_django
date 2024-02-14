from import_export import resources
from sem.models import CertificadoListaBlanca, Exento

        

class CertificadoListaBlancaResource(resources.ModelResource):
    class Meta:
        model = CertificadoListaBlanca
        


class ExentoResource(resources.ModelResource):
    class Meta:
        model = Exento
