from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sem.views import CertificadoListaBlancaViewSet, ExentoViewSet

router = DefaultRouter()
router.register(r'certificados', CertificadoListaBlancaViewSet)
router.register(r'exentos', ExentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
