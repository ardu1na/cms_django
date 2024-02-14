from import_export import resources
from digesto.models import  ItemDigesto, Tema, Archivo



class ArchivoResource(resources.ModelResource):
    class Meta:
        model = Archivo


class TemaResource(resources.ModelResource):
    class Meta:
        model = Tema


class ItemDigestoResource(resources.ModelResource):
    class Meta:
        model = ItemDigesto
