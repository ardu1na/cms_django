
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings
from core.views import my_404_view, my_500_view, \
    fake_admin

from prensa.views import index, articulo, prensa,  tags

from prensa.api.utils import schema_view
from prensa.api.viewsets import lastArticulosView, lastArticulosList, \
    DestacadosArticulosView, tagsList

from sem import urls 

handler404 = my_404_view
handler500 = my_500_view


urlpatterns = [

################## DJANGO FE 
    #
    # pagina de inicio
    path('', index, name="index"),
    #
    # página de prensa (CMS)
    path('prensa/nota/<slug:slug>/', articulo, name="articulo"),
    path('prensa/', prensa, name="prensa"),
    path('prensa/tag/<slug:slug>/', tags, name="tag"),

############################# OTHER UI FE (REACT)
    #     # API DE PRENSA

    # api docs
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # endpoint para el servicio CMS Prensa
    path('api/prensa/', include('prensa.urls')), # VER DOCS

    ## micro servicios

    # DEVUELVE TITULO E IMAGEN DE LOS 3 ULTIMOS DESTACADOS
    path('api/prensa/destacados/', DestacadosArticulosView, name="destacados"),

    # DEVUELVE TITULO E IMAGEN DE LOS ULTIMOS 3
    path('api/prensa/last/', lastArticulosView, name="last"), 


    # DEVUELVE LOS TITULOS DE LOS ULTIMOS 7
    path('api/prensa/last/list/', lastArticulosList, name="last-list"), 
    
    # DEVUELVE LOS TITULOS DE LOS TAGS
    path('api/prensa/tags/list/', tagsList, name="tags-list"), 

#     # API DE SEM
    path('api/sem/', include('sem.urls'), name="sem"), 


#     # API DE DIGESTO MUNICIPAL
    path('api/digesto/', include('digesto.urls'), name="digesto"),



#     # API DE CULTURA EVENTOS
    path('api/cultura/', include('cultura.urls'), name="cultura"),

################ backend management

    # panel de administración / CMS, users, perms, etc
    path('acceso_interno/', admin.site.urls),
    
    # admin honeypots 
    path('cpanel/', fake_admin),
    path('admin/', fake_admin),
    path('administrator/', fake_admin),
    path('wp-admin/', fake_admin),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # manejar esto diferente en prod
