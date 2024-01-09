from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sem.views import CertificadoListaBlancaViewSet

router = DefaultRouter()
router.register(r'certificados', CertificadoListaBlancaViewSet)

urlpatterns = [
    path('certificados/', include(router.urls)),
]
