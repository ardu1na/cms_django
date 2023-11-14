
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from prensa.views import index, articulo, prensa, categorias


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prensa/', include('prensa.urls')),
    path('', index, name="index"),
    path('prensa/nota/<slug:slug>/', articulo, name="articulo"),
    path('prensa/', prensa, name="prensa"),
    path('prensa/categoria/<slug:slug>/', categorias, name="categoria"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
