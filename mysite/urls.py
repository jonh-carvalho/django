
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
   openapi.Info(
      title="API para o censo da Ilha Primeira",
      default_version='v1',
      description="API para gerenciamento dos dados do censo demográfico da Ilha Primeira",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@empresa.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('render.urls')),
    path('api/', include('censo.api_urls')),  # URLs da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
