
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import render, redirect

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import settings

from prensa.views import index, articulo, prensa,  tags

from prensa.api.viewsets import lastArticulosView, lastArticulosList, \
    DestacadosArticulosView, tagsList



# páginas de error

def _404_view(request, exception):
    return render (request, '404.html', status=404)

def _500_view(request):
    return render (request, '500.html', status=500)

handler404 = _404_view
handler500 = _500_view



###

def fake_admin(request):
    if request.method == 'GET':
        return render(request, 'f_login.html')
    return redirect('index')



## documentación 

schema_view = get_schema_view(
   openapi.Info(
      title="DJANGO CMS API",
      default_version='v1',
      description="Beta version of endpoints",
      contact=openapi.Contact(email="arduinadelbosque@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
###############################################################################################################
########### PATHS 

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

    # micro servicios
    path('api/prensa/destacados/', DestacadosArticulosView, name="destacados"), # DEVUELVE TITULO E IMAGEN DE LOS 3 ULTIMOS DESTACADOS
    path('api/prensa/last/', lastArticulosView, name="last"), # DEVUELVE TITULO E IMAGEN DE LOS ULTIMOS 3

    path('api/prensa/last/list/', lastArticulosList, name="last-list"), # DEVUELVE LOS TITULOS DE LOS ULTIMOS 7
    path('api/prensa/tags/list/', tagsList, name="tags-list"), # DEVUELVE LOS TITULOS DE LOS TAGS



################ backend management

    # panel de administración / CMS, users, perms, etc
    path('acceso_interno/', admin.site.urls),
    
    # admin honeypots 
    path('cpanel/', fake_admin),
    path('admin/', fake_admin),
    path('administrator/', fake_admin),
    path('wp-admin/', fake_admin),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # manejar esto diferente en prod
