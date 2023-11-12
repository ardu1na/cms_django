from rest_framework.routers import DefaultRouter

from prensa.api.viewsets import ArticulosViewSet
router = DefaultRouter()
router.register(r'articulos', ArticulosViewSet, basename='articulo')

urlpatterns = router.urls