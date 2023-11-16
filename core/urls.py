
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import render, redirect

from core import settings
from prensa.views import index, articulo, prensa, categorias, tags



# páginas de error

def _404_view(request, exception):
    return render (request, '404.html', status=404)

def _500_view(request):
    return render (request, '500.html', status=500)

handler404 = _404_view
handler500 = _500_view




def fake_admin(request):
    if request.method == 'GET':
        return render(request, 'f_login.html')
    return redirect('index')

urlpatterns = [
    # panel de administración
    path('acceso_interno/', admin.site.urls),
    
    # admin honeypots 
    path('cpanel/', fake_admin),
    path('admin/', fake_admin),
    path('administrator/', fake_admin),
    path('wp-admin/', fake_admin),

    # pagina de inicio
    path('', index, name="index"),

    # página de prensa
    path('prensa/nota/<slug:slug>/', articulo, name="articulo"),
    path('prensa/', prensa, name="prensa"),
    path('prensa/categoria/<slug:slug>/', categorias, name="categoria"),
    path('prensa/tag/<slug:slug>/', tags, name="tag"),

    # endpoint para el servicio CMS Prensa
    path('api/prensa/', include('prensa.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # manejar esto diferente en prod
