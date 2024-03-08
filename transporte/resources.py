from import_export import resources
from transporte.models import   Valor



class ValorResource(resources.ModelResource):
    class Meta:
        model = Valor

