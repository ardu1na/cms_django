from rest_framework.routers import DefaultRouter

from cultura.api.viewsets import EventosViewSet

router = DefaultRouter()
router.register(r'eventos', EventosViewSet, basename='evento')

urlpatterns = router.urls