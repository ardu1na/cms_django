
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import render

from core import settings
from prensa.views import index, articulo, prensa, categorias, tags


def my_404_view(request, exception):
    return render (request, '404.html', status=404)

def my_500_view(request):
    return render (request, '500.html', status=500)


handler404 = my_404_view
handler500 = my_500_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prensa/', include('prensa.urls')),
    path('', index, name="index"),
    path('prensa/nota/<slug:slug>/', articulo, name="articulo"),
    path('prensa/', prensa, name="prensa"),
    path('prensa/categoria/<slug:slug>/', categorias, name="categoria"),
    path('prensa/tag/<slug:slug>/', tags, name="tag"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
