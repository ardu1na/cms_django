from import_export import resources
from prensa.models import  Articulo

        

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo
        