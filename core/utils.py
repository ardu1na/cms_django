from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

## documentación 

schema_view = get_schema_view(
   openapi.Info(
      title="DJANGO CMS API",
      default_version='v1',
      description="Beta version of endpoints",
      contact=openapi.Contact(email="arduinadelbosque@gmail.com"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
    )
