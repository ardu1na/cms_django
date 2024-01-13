from rest_framework.routers import DefaultRouter

from digesto.views import DigestoViewSet
router = DefaultRouter()
router.register(r'', DigestoViewSet, basename='digesto')

urlpatterns = router.urls