from import_export import resources
from cultura.models import Evento

        

class EventoResource(resources.ModelResource):
    class Meta:
        model = Evento
        