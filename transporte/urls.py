from rest_framework.routers import DefaultRouter

from transporte.views import ValorViewSet

router = DefaultRouter()
router.register(r'valores', ValorViewSet)
urlpatterns = router.urls