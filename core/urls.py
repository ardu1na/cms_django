
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import render, redirect

from core import settings
from prensa.views import index, articulo, prensa, categorias, tags

def fake_admin(request):
    if request.method == 'GET':
        return render(request, 'f_login.html')
    return redirect('index')

def _404_view(request, exception):
    return render (request, '404.html', status=404)

def _500_view(request):
    return render (request, '500.html', status=500)


handler404 = _404_view
handler500 = _500_view


urlpatterns = [
    path('backend/', admin.site.urls),
    path('admin/', fake_admin, name="administrator"),
    path('api/prensa/', include('prensa.urls')),
    path('', index, name="index"),
    path('prensa/nota/<slug:slug>/', articulo, name="articulo"),
    path('prensa/', prensa, name="prensa"),
    path('prensa/categoria/<slug:slug>/', categorias, name="categoria"),
    path('prensa/tag/<slug:slug>/', tags, name="tag"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
