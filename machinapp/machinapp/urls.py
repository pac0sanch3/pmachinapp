"""
URL configuration for machinapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#importaciones de las rutas de las apps
from apps.roles.api.router import router_rol
from apps.sedes.api.router import router_sede
from apps.areas.api.router import router_areas
from apps.mantenimientos.api.router import router_mantenimiento

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="MachinApp",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="emerssonramirez510@gmail.com"),
      license=openapi.License(name="Machinapp"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_rol.urls)),
    path('api/', include(router_mantenimiento.urls)),
    path('api/', include(router_sede.urls)),
    path('api/', include(router_areas.urls)),


    path('api/user/', include('apps.user.api.router')),
    path('api/', include('apps.centros.api.router')),
    path('api/', include('apps.tipositio.api.router')),
    path('api/ambiente/', include('apps.ambientes.api.router')),
    path('api/', include('apps.tipomantenimiento.api.router')),
    path('api/', include('apps.tipoequipo.api.router')),
    path('api/', include('apps.fichas.api.router')),
    path('api/', include('apps.variables.api.router')),
    path('api/detalle/', include('apps.detalles.api.router')),
    path('api/', include('apps.actividades.api.router')),
    #documentacion
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)