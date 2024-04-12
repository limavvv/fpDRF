
from django.contrib import admin
from django.urls import path, include

from movie.views import *
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Description of your API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# router = routers.DefaultRouter()
# router.register(r'movies', MovieViewSet)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls))
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/' ,include('movie.urls')),
    path('api/v1/', include('user.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
