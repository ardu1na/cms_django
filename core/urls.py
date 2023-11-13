
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings


from django.shortcuts import render

def test(request):
    return render (request,'page/index.html',{})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prensa/', include('prensa.urls')),
    
    path('', test)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
