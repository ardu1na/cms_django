from rest_framework.routers import DefaultRouter

from digesto.views import DigestoViewSet, TemasDigestoViewSet
router = DefaultRouter()
router.register(r'items', DigestoViewSet)
router.register(r'temas', TemasDigestoViewSet)
urlpatterns = router.urls